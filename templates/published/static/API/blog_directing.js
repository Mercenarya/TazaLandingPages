// function redirecting_blog_1(){
//     try{
//         window.location.href = "/templates/forums/forum_blog_1.html";
//     }catch(error){
//         alert(`An error occurred :\n ${error}`);
//         console.error(error);
//     }
// }

// function redirecting_blog_2(){
//     try{
//         window.location.href = "/templates/forums/forum_blog_2.html";
//     }
//     catch(error){
//         alert('An error occured :\n ${error}');
//         console.error(error);
//     }
// }

// main forums
function redirecting_pages(path){
    try{
        window.location.href = `${path}`;
    }
    catch(error){
        alert(`An error occured :\n ${error}`);
        console.error(error)
    }
}