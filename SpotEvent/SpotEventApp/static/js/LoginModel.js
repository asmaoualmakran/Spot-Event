
var viewModel = new function()
{
    var self = this;
    

    self.data = {
    username : ko.observable('Thoraxis'),
    first_name : ko.observable('Robin'),
    last_name : ko.observable('Cortvrindt'),
    email : ko.observable('cortvrindt.robin@gmail.com'),
    birthday : ko.observable('1995-11-28'),
    password : ko.observable('password'),
    street : ko.observable('Vijverstraat'),
    number : ko.observable('27'),
    city : ko.observable('Asse'),
    zip_code : ko.observable('1730'),
    country : ko.observable('Belgium'),
    }


    self.data2 = {
        'email' : ko.observable('test@tester.com'),
        'password' : ko.observable('password'),
    }

    self.redirect = function() {
        window.location.href="browse"
    }




    self.register = function(){
    	$.post('/api/user',ko.toJS(self.data),self.redirect)
    };

    self.login = function(){
        $.post('/api/user/authenticate',ko.toJS(self.data2),self.redirect)
    };



}

ko.applyBindings(viewModel);  