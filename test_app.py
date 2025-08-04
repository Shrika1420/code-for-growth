from app import app

def test_home():
    # Create a test client
    tester = app.test_client()
    response = tester.get('/')
    
    #Check status code
    assert response.status_code == 200
    
    # Chcek the content
    
    assert response.get_json() == {"message" : "Hello, CI/CD World!"} 
    
    