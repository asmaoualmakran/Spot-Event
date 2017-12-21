var viewModel = new function()
{
    var self = this;

    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

}

ko.applyBindings(viewModel);  