
var viewModel = new function()
{
    var self = this;

    self.error = ko.observable();

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

    self.errorsvisible=ko.observable(false);
    

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
        'email' : ko.observable('cortvrindt.robin@gmail.com'),
        'password' : ko.observable('password'),
    }

    self.redirect = function() {
        window.location.href="browse"
    }

    self.register = function(){
    	$.post('/api/user',ko.toJS(self.data),self.redirect).fail(function(response){
            self.failure(response);
        });
    };

    self.login = function(){
        $.post('/api/user/authenticate',ko.toJS(self.data2), self.redirect).fail(function(response){
            self.failure(response);
        });
    };



}

ko.applyBindings(viewModel);  