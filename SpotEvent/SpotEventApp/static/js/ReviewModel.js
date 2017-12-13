var viewModel = new function()
{
    var self = this;
    self.score = ko.observable("");
    self.reviewText = ko.observable("");

}

ko.applyBindings(viewModel);  