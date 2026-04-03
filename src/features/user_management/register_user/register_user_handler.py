from .register_user_request import RegisterUserRequest

class RegisterUserHandler:
    
    def handle(self, request: RegisterUserRequest):
        # Here you would add logic to save the user to the database
        return {"message": f"User {request.username} registered successfully"}