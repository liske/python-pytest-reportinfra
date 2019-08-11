import re
import requests
from datetime import timedelta


class ReportInfraConfig():
    url = 'http://localhost:8000/api/result/'
    token = None
    sslverify = True


ri_conf = ReportInfraConfig()


def pytest_addoption(parser):
    """Adds options to control reportinfra."""
    group = parser.getgroup('terminal reporting')
    group.addoption('--ri-url',
                    dest='ri_url',
                    default=ReportInfraConfig.url,
                    help='url of reportinfra')
    group.addoption('--ri-token',
                    dest='ri_token',
                    default=ReportInfraConfig.token,
                    help='auth token for reportinfra access')
    group.addoption('--ri-ssl-verify',
                    dest='ri_sslverify',
                    default=ReportInfraConfig.sslverify,
                    help='auth token for reportinfra access')


def pytest_configure(config):
    ri_conf.url = config.option.ri_url
    ri_conf.token = config.option.ri_token
    ri_conf.sslverify = config.option.ri_sslverify


def pytest_terminal_summary(terminalreporter):
    results = {}

    for outcome in ['failed', 'passed', 'skipped']:
        if outcome in terminalreporter.stats:
            for test in terminalreporter.stats[outcome]:
                result = {
                    "outcome": test.outcome,
                    "duration": str(timedelta(seconds=test.duration))
                }
                if test.user_properties:
                    result = {**dict(test.user_properties), **result}

                # generate fallback control name if required
                if not "control" in result:
                    # strip module prefix
                    result["control"] = re.sub(
                        r'^.+::test__([^[]+).*$', '\\1', test.nodeid)
                    # replace '__' by slash
                    result["control"] = re.sub(r'__', '/', result["control"])

                # add trace if available
                if test.longrepr is not None:
                    result["trace"] = str(test.longrepr)

                name = re.sub(r'^.+\[\w+://([^]]+).*$', '\\1', test.nodeid)
                if not name in results:
                    results[name] = {"device": name, "tests": []}
                results[name]['tests'].append(result)

    # prepare auth header                
    headers = None
    if ri_conf.token is not None:
        headers = {'Authorization': 'Token {}'.format(ri_conf.token)}

    # push results
    for res in results.values():
        resp = requests.post(ri_conf.url, json=res, headers=headers)
