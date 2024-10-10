


from providers import auth_provider


class Controller:
    @staticmethod
    def authorization(key, method, path):
        user, status_code = Controller.authorise_user(key)
        if user is None:
            return ("unauthorized"), status_code
        
        has_access, method_status_code = Controller.authorise_method(user, path, method)
        if not has_access:
            return ({"message": "Forbidden"}), method_status_code
        
    @staticmethod
    def authorise_user(api_key):

        user = auth_provider.get_user(api_key)
        if user == None:    
            return None, 401
        return user, 200
    
    @staticmethod
    def authorise_method(user, path, method):
        if not auth_provider.has_access(user, path, method):
            return False, 403
        return True, 200

  