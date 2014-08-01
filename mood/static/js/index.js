//$(document).ready(function(){
//    var client_id = '6ebf0401b77d420bb58952187230c1f0';
//    var secret = 'b89efa5deeb547c7a017dc6a0ddaf89f';
//    $.ajax({
//        url: "https://api.spotify.com/v1/search",
//        data:{
//            q: 'garden state soundtrack',
//            type:'album'
//        },
//
//        success: function(data){
//            console.log(data);
//            movie_album_id = data["albums"]["items"][0]["id"];
//        },
//        error: function(data){
//            console.log(data);
//        }
//
//    });
//});
//
//
//
//    $('#searchButton').on("click", function () {
//        var album_query = $('#search').val()+ " motion picture";
//        var movie_album_id;
//        $.ajax({
//            url: "https://api.spotify.com/v1/search",
//            data: {
//                q: album_query,
//                type: 'album',
//                limit: '1'
//            },
//
//            success: function (data) {
//                console.log(album_query);
//                console.log(data);
//                console.log(data["albums"]["items"][0]["id"]);
//                movie_album_id = data["albums"]["items"][0]['id'];
//                movieInfo.title = $('#search').val();
//                movieInfo = JSON.stringify(movieInfo);
//
//
//
//            },
//            error: function (data) {
//                console.log(data);
//            }