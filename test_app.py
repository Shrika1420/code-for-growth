from app import app

def test_dashboard():
    with app.test_client() as client:
        response = client.get('/dashboard')
        html = response.data.decode('utf-8')
        
    
    #Check status code
    assert response.status_code == 200
    
    # Check the content
    assert "Logistics Dashboard" in html
    assert "Total Shipments" in html
    assert "Delayed Shipments" in html
    assert "Average Delay" in html  
    
    
    