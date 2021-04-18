from racing_pkg import report

def test_landing(client):

    landing = client.get("/")
    html = landing.data.decode()

    assert landing.status_code == 200
    assert "<table>" in html
    assert "<th>Abbreviation</th>" in html
    assert "<th>Result Time</th>" in html
    assert "possible errors in data:" in html
    assert "<li>" in html


def test_landing_rep_desc(client):

    landing_rep_desc = client.get("/report?order=desc")
    html = landing_rep_desc.data.decode()

    assert landing_rep_desc.status_code == 200
    assert "<table>" in html
    assert "<th>Abbreviation</th>" in html
    assert "<th>Result Time</th>" in html
    assert "possible errors in data:" in html
    assert "<li>" in html


def test_landing_dr(client):

    landing_dr = client.get("/report/drivers")
    html = landing_dr.data.decode()

    assert landing_dr.status_code == 200
    assert ">reverse result</a>" in html
    assert "<table>" in html
    assert "<th>Abbreviation</th>" in html
    assert "<th>Name</th>" in html
    assert "<th>Company</th>" in html


def test_landing_dr_desc(client):
    landing_dr_desc = client.get("/report/drivers?order=desc")
    html = landing_dr_desc.data.decode()

    assert landing_dr_desc.status_code == 200
    assert ">reverse result</a>" in html
    assert "<table>" in html
    assert "<th>Abbreviation</th>" in html
    assert "<th>Name</th>" in html
    assert "<th>Company</th>" in html


def test_landing_driver(client):
    whole_list = report.load_data("data")

    for item in whole_list:
        landing_driver = client.get("/report/drivers?driver_id="+item.Abbreviation)
     
        assert landing_driver.status_code == 200  
 