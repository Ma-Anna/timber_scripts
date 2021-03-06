import json
from requests import Request, Session

CREATE_TENDER_URL_FOR_SB = "https://procedure-sandbox.prozorro.sale"
CREATE_TENDER_URL_FOR_STAGE = "https://procedure-staging.prozorro.sale"
KEY = "9fa74b0e-e692-4746-b38b-8a4387097a53"
TENDERS_COUNT = 50


def create_tender():
    with open("data/create_tender.json", 'r', encoding='utf-8') as f_obj:
        jsn = f_obj.read()

    data = json.loads(jsn)
    headers = {
        "Authorization": KEY,
        "Content-Type": "application/json"
    }

    s = Session()
    r = Request('POST', "{}/api/procedures".format(CREATE_TENDER_URL_FOR_STAGE), json=data, headers=headers)
    prepped = r.prepare()
    resp = s.send(prepped)
    print(resp.content)
    return json.loads(resp.content)['id']


if __name__ == '__main__':
    tender_ids = list()
    for i in range(TENDERS_COUNT):
        tender_ids.append(create_tender())
    print(tender_ids)



#Changing line 112 to self.encoder = json.load(open(vocab_file, 'r', encoding='utf-8')) should fix this issue.

