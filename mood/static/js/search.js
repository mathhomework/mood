$(document).ready(function() {

    var client_id = '6ebf0401b77d420bb58952187230c1f0';
    var secret = 'b89efa5deeb547c7a017dc6a0ddaf89f';
    var album_query;
    var movieInfo = {};
    var songInfo = {};
    $('#searchButton').on("click", function () {
        album_query = $('#search').val();
        var album_query_js = JSON.stringify({'album_query':album_query});
        $.ajax({
            url: "/search_results/",
            type: "POST",
            dataType: "json",
            data: album_query_js,
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});





//
//
//$(document).ready(function() {
//
//    var client_id = '6ebf0401b77d420bb58952187230c1f0';
//    var secret = 'b89efa5deeb547c7a017dc6a0ddaf89f';
//
//    var movieInfo = {};
//    var songInfo = {};
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
//        }).complete(function() {
//            $.ajax({
//                url: "https://api.spotify.com/v1/albums/"+movie_album_id+"/tracks",
//                data: {
//                    limit: '40'
//                },
//
//                success: function (data) {
//                    console.log(data);
//                    console.log(data["items"][0]["artists"][0]["name"]);
//                    console.log(data["items"][0]["name"]);
//                    for(var x=0; x< data["items"].length; x++){
//                        songInfo.artist = data["items"][x]["artists"][0]["name"];
//                        songInfo.title = data["items"][0]["name"];
//                        songInfo = JSON.stringify(movieInfo);
//                    }
//
//                },
//                error: function (data) {
//                    console.log(data);
//                }
//            }).complete(function() {
//                $.ajax({
//                    url: "search_results",
//                    type: "POST",
//                    dataType: "html",
//                    data: {'query': query},
//                    success: function (data) {
//                        console.log("hello" + data);
//                    },
//                    error: function (data) {
//                        console.log(data);
//                    }
//
//                });
//            });
//
//
//        });
//
//    });
//});