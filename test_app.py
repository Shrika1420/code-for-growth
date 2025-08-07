from app import app

def test_dashboard():
    with app.test_client() as client:
        response = client.get('/dashboard')
        
    
    #Check status code
    assert response.status_code == 200
    
    # Checkk the content
    assert response.data.decode('utf-8') == '<h1>Welcome to the Logistics Dashboard</h1>'
    assert b'<img src="/logistics/delay-plot">' in response.data
    assert b'<p>Total Shipments: 0</p>' in response.data
    assert b'<p>Delayed Shipments: 0</p>' in response.data
    assert b'<p>Average Delay: 0.0 minutes</p>' in response.data    
    
    
    