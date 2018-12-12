//These would be the buttons to either create a new instance of a product
//or delete a product
$(function() {
	//Create/add new product - would create a new instance of Product model
	//would make a call to the add method to add product
    $("#create").click(add)
	//On click would delete a product, this would call
	//the deleteItem method to remove a product 
    $(".delete").click(deleteItem)
	//By clicking any items within tag would result
	//in the getProd being called which would essentially
	//get all product information
    $("li").click(getProd)
	//This would allow the information, gained through the getProd
	//function, to be updated. This would call the update function when it is clicked.
    $("#update").click(update)
})

//This function would get the existing products in the database 
function getProd(){
  id = $(this).attr("id")
  request = {
    url: "getProduct/" + id,
    type: "GET",
    success: function (response){
      $(".existingProd").attr("id", response.id)
      $("#updateName").val(response.name)
      $("#updateDescription").val(response.desc)
      $("#updatePrice").val(response.price)
    },
    error: error
  }
  var csrf = "input[name=csrfmiddlewaretoken]"
  $.ajax(request)
}

//This would allow the user to add new products.
function add() {
  request = {
    url: "addProduct/",
    type: "POST",
    data: {
      name: $("#name").val(),
      description: $("#description").val(),
      price: $("#price").val()
    },
    success: function (response){
      var added = "<li id='" + response.id + "'>" + response.name + "<button class='delete' type=button>Delete</button></li>";
      $("#showProducts").append(added)
      $("li").click(getProd)
      $(".delete").click(deleteItem)
    },
    error:  error
  }
  var csrf = "input[name=csrfmiddlewaretoken]"
  $.ajax(request)
}

//This module will delete a product from the database
//when the button is clicked
function deleteItem(){
  id = $(this).parent().attr("id")
  request = {
    url: "deleteProduct/" + id + "/",
    type: "DELETE",
    success: delMessage,
    error: error
  }
  var csrf = "input[name=csrfmiddlewaretoken]"
  $.ajax(request)
  $(this).parent().remove()
}

function delMessage(){
	alert("Product has been deleted!")
}

//This will update the data for a product instance
function update(){
  id = $(".existingProd").attr("id")
  request = {
    url: "updateProduct/" + id + "/",
    type: "PUT",
    data: {
      id: $(".existingProd").attr("id"),
      name: $("#updateName").val(),
      description: $("#updateDescription").val(),
      price: $("#updatePrice").val()
    },
    success: function (response) {
      $("#" + response.id).text(response.name)
      $("#" + response.id).append("<button class='delete' type=button>Delete</button>")
      $(".delete").click(deleteItem)
    },
    error: error
  }
  var csrf = "input[name=csrfmiddlewaretoken]"
  $.ajax(request)
}

//This will be called if there is an error in the request response
function error() {
  alert("There is an error for the request");
}