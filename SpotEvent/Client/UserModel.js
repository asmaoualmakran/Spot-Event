var viewModel = new function()
{
    var self = this;
    self.firstName = ko.observable("default first");
    self.lastName = ko.observable("default last");
    self.responseJSON = ko.observable(null);
    self.onSubmit = function() 
    {
        var data = JSON.stringify(
            {
                first : self.firstName(), last : self.lastName()        
            }); // prepare request data
        $.post("/echo/json", data, function(response) // sends 'post' request
        {
            // on success callback
            self.responseJSON(response);
        })
    }
}

ko.applyBindings(viewModel);  