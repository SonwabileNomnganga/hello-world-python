from app import greet 

def test_greet(): 
    result = greet("World") 
    assert "Hello, World!" in result, "Greeting message incorrect" 
    print("✅ Test passed!") 

test_greet()