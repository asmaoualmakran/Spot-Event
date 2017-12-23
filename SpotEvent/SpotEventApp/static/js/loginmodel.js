
var viewModel = new function()
{
    var self = this;

    //used to store the error response from the server
    self.error = ko.observable();

    //reads the error respond and inserts it in an alert box
    self.failure = function(errors){
        self.error(errors.responseText);
        console.log(self.error());
        var d = document.createElement('DIV');
        d.innerHTML = self.error();
        d.innerHTML = d.innerHTML.replace(/,/g,"<br>")
        d.innerHTML = d.innerHTML.replace('{',"")
        d.innerHTML = d.innerHTML.replace(/"/g," ")
        d.innerHTML = d.innerHTML.replace('}'," ")
        document.getElementById('container').insertBefore(d, document.getElementById('div_1'));
        self.errorsvisible(true);
    }

    // the variable which decides whether or not the error box is visible
    self.errorsvisible=ko.observable(false);
    
    // contains the data from the register form
    self.data = {
    username : ko.observable(),
    first_name : ko.observable(),
    last_name : ko.observable(),
    email : ko.observable(),
    birthday : ko.observable(),
    password : ko.observable(),
    street : ko.observable(),
    number : ko.observable(),
    city : ko.observable(),
    zip_code : ko.observable(),
    country : ko.observable(),
    }

    // contains the data from the login form
    self.data2 = {
        'email' : ko.observable(),
        'password' : ko.observable(),
    }

    // redirect you to the browse page after logging in
    self.redirect = function() {
        window.location.href="browse"
    }

    // send register request to the server
    self.register = function(){
    	$.post('/api/user',ko.toJS(self.data),self.redirect).fail(function(response){
            self.failure(response);
        });
    };

    // send login request to the server
    self.login = function(){
        $.post('/api/user/authenticate',ko.toJS(self.data2), self.redirect).fail(function(response){
            self.failure(response);
        });
    };



}

ko.applyBindings(viewModel);  