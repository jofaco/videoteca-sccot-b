import vimeo



def cons_vim_api(videoid):

    client = vimeo.VimeoClient(
        token='438a13e91fb038b956189c3eba8becdc',
        key='130c6e80c9de8a4080958e5e497368d99374a15d',
        secret='Xoc2x8udkKQPKR3jmJSriCgtcKBDm1WjESbjQ3V7WOVzG91P7GCMn1xMLV8u4uaxuj0JlCvx5uUn0PoPZsTb2AwsoGW6nIh/UOy5hV4eGO2r2izsiR4suh95DvSUsBqS'
    )
    response = client.get('https://api.vimeo.com/videos/'+videoid).json()
    
    return response
