$(document).ready(function(){
    var client_id = '6ebf0401b77d420bb58952187230c1f0';
    var secret = 'b89efa5deeb547c7a017dc6a0ddaf89f';
    $.ajax({
        url: "https://api.spotify.com/v1/search",
        data:{
            q: 'garden state soundtrack',
            type:'album'
        },

        success: function(data){
            console.log(data);
        },
        error: function(data){
            console.log(data);
        }

    });
});