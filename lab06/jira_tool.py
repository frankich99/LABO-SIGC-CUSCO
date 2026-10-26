import os
import base64
import json
import urllib.request
import urllib.error

DOMAIN = os.environ.get("JIRA_DOMAIN", "https://unsaac-team-grupois.atlassian.net")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")
EMAIL = os.environ.get("JIRA_EMAIL", "133962@unsaac.edu.pe")

AUTH = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()

def api_call(path, method="GET", body=None):
    url = f"{DOMAIN}{path}"
    headers = {
        "Authorization": f"Basic {AUTH}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode()
            if content:
                return json.loads(content)
            return {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        print(f"HTTPError {e.code} on {path}: {err_msg}")
        return {"error": e.code, "message": err_msg}
    except Exception as e:
        print(f"Error on {path}: {e}")
        return {"error": str(e)}

def get_transitions(issue_key):
    res = api_call(f"/rest/api/3/issue/{issue_key}/transitions")
    return res.get("transitions", [])

def transition_issue(issue_key, transition_name):
    transitions = get_transitions(issue_key)
    target = next((t for t in transitions if t["name"].lower() == transition_name.lower()), None)
    if not target:
        print(f"Transition '{transition_name}' not found for {issue_key}. Available: {[t['name'] for t in transitions]}")
        return False
    body = {"transition": {"id": target["id"]}}
    res = api_call(f"/rest/api/3/issue/{issue_key}/transitions", method="POST", body=body)
    if "error" not in res:
        print(f"Successfully transitioned {issue_key} to '{target['name']}'")
        return True
    return False

def assign_issue(issue_key, account_id):
    body = {"accountId": account_id}
    res = api_call(f"/rest/api/3/issue/{issue_key}/assignee", method="PUT", body=body)
    if "error" not in res:
        print(f"Assigned {issue_key} to {account_id}")
        return True
    return False

def check_board_137():
    config = api_call("/rest/agile/1.0/board/137/configuration")
    print("=== BOARD 137 CONFIGURATION ===")
    print(f"Board ID: {config.get('id')} | Name: {config.get('name')} | Type: {config.get('type')}")
    cols = config.get("columnConfig", {}).get("columns", [])
    for c in cols:
        s_ids = [s.get("id") for s in c.get("statuses", [])]
        print(f"Column: {c.get('name')} | Min: {c.get('min')} | Max: {c.get('max')} | Statuses: {s_ids}")

    issues = api_call("/rest/agile/1.0/board/137/issue?maxResults=100").get("issues", [])
    print(f"\nTotal issues visible on Board 137: {len(issues)}")
    for i in issues[:10]:
        print(f"  [{i['key']}] {i['fields']['summary']} - Status: {i['fields']['status']['name']} - Assignee: {i['fields'].get('assignee', {}).get('displayName', 'Sin asignar') if i['fields'].get('assignee') else 'Sin asignar'}")

def list_assignable_users():
    users = api_call("/rest/api/3/user/assignable/search?project=SC")
    print("=== ASSIGNABLE USERS IN PROJECT SC ===")
    for u in users:
        print(f"Name: {u.get('displayName')} | AccountId: {u.get('accountId')} | Email: {u.get('emailAddress')}")

def check_sprint_282():
    issues = api_call("/rest/agile/1.0/sprint/282/issue").get("issues", [])
    print(f"Sprint 282 now has {len(issues)} issues:")
    for i in issues:
        status_name = i['fields']['status']['name']
        assignee_name = i['fields'].get('assignee', {}).get('displayName', 'Sin asignar') if i['fields'].get('assignee') else 'Sin asignar'
        print(f"  [{i['key']}] {i['fields']['summary']} -> Status: {status_name} | Assignee: {assignee_name}")

def start_sprint_282():
    body = {
        "state": "active",
        "startDate": "2026-10-26T12:00:00.000Z",
        "endDate": "2026-11-09T12:00:00.000Z"
    }
    res = api_call("/rest/agile/1.0/sprint/282", method="POST", body=body)
    print("Start sprint 282 res:", res)

def add_completed_to_sprint_282():
    completed_keys = ['SC-2', 'SC-3', 'SC-4', 'SC-5', 'SC-6']
    res = api_call("/rest/agile/1.0/sprint/282/issue", method="POST", body={"issues": completed_keys})
    print("Add completed to sprint 282 res:", res)

def verify_active_board_136():
    issues = api_call("/rest/agile/1.0/board/136/issue?maxResults=100").get("issues", [])
    print(f"Total issues on Board 136: {len(issues)}")
    by_status = {}
    for i in issues:
        st = i['fields']['status']['name']
        by_status.setdefault(st, []).append(f"[{i['key']}] {i['fields']['summary']} ({i['fields'].get('assignee', {}).get('displayName', 'Sin asignar') if i['fields'].get('assignee') else 'Sin asignar'})")

    for st, items in by_status.items():
        print(f"\n--- {st.upper()} ({len(items)}) ---")
        for it in items[:6]:
            print(" ", it)
        if len(items) > 6:
            print(f"  ... y {len(items)-6} más")

def verify_sprint_283_active():
    res = api_call("/rest/agile/1.0/sprint/283")
    print(f"Sprint 283 state: {res.get('state')}")
    issues = api_call("/rest/agile/1.0/sprint/283/issue").get("issues", [])
    print(f"Total active issues in Sprint 283: {len(issues)}")
    by_status = {}
    for i in issues:
        st = i['fields']['status']['name']
        by_status.setdefault(st, []).append(i['key'])
    for st, keys in by_status.items():
        print(f"  {st}: {len(keys)} issues -> {keys[:6]}")

def add_sc19_to_sprint_283():
    res = api_call("/rest/agile/1.0/sprint/283/issue", method="POST", body={"issues": ["SC-19"]})
    print("Add SC-19 to sprint 283 res:", res)

if __name__ == "__main__":
    verify_sprint_283_active()
