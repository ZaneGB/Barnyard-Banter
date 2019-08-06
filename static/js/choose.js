var idx = index;
//console.log("HI "+indx);
var targetDiv = d3.select(".cat-div");
targetDiv.html("<a href='http://localhost:5000/value/cat_"+idx+".jpg'><img src='../static/test/cat/cat_"+idx+".jpg' class='img-thumbnail' /></a>");
  
var targetDiv = d3.select(".cow-div");
targetDiv.html("<a href='http://localhost:5000/value/cow_"+idx+".jpg'><img src='../static/test/cow/cow_"+idx+".jpg' class='img-thumbnail' /></a>");
  
var targetDiv = d3.select(".dog-div");
targetDiv.html("<a href='http://localhost:5000/value/dog"+idx+".jpg'><img src='../static/test/dog/dog"+idx+".jpg' class='img-thumbnail' /></a>");
  
var targetDiv = d3.select(".shp-div");
targetDiv.html("<a href='http://localhost:5000/value/sheep"+idx+".jpg'><img src='../static/test/sheep/sheep"+idx+".jpg' class='img-thumbnail' /></a>");
  
    
// d3.selectAll(".img-thumbnail").on("click",function(){
// var surl = d3.select(this).attr("src");
// var simage = this;
// var surlend = surl.split("/").pop();
// console.log(surlend);

// $.ajax({
//     url: 'http://localhost:5000/value/' + surlend,
//     headers: {
//         'Content-Type': 'application/x-www-form-urlencoded'
//     },
//     type: "POST", /* or type:"GET" or type:"PUT" */
//     dataType: "json",
//     data: {},
//     success: function (result) {
//         console.log(result);    
//     },
//     error: function () {
//         console.log("error");
//     }
//   });
// console.log(surl);
// })