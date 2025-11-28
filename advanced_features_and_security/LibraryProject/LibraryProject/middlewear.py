class ContentSecurityPolicyMiddleware:
    """
    Sets a conservative Content-Security-Policy header.
    Adjust the sources according to the domains your app needs (CDNs, analytics, etc).
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # adjust policy as needed
        self.csp_policy = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )

    def __call__(self, request):
        response = self.get_response(request)
        # Do not overwrite an existing CSP header if present
        if 'Content-Security-Policy' not in response:
            response['Content-Security-Policy'] = self.csp_policy
        return response
