
var viewModel = new function()
{
    var self = this;

    self.data;

    self.dummy= {
    	street : 'Vijverstraat',
    	number : 27,
    	zipcode : 1730,
    	country : 'Belgium'

    }
    
    self.street = ko.observable(self.dummy.street);
    self.number = ko.observable(self.dummy.number);
    self.zipcode = ko.observable(self.dummy.zipcode);
    self.country = ko.observable(self.dummy.country);



    self.getAddress = function(){
    	console.log("getAddress")
    	$.get('/api/address',self.data)
    }

}

ko.applyBindings(viewModel);  