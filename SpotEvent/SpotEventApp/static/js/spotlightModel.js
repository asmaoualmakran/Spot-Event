var viewModel = new function()
{
    var self = this;
    
    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

    self.events = ko.observableArray();

    function createEvents(data) {
        self.events(data);
    }

}

ko.applyBindings(viewModel);  