function Add(Idproduct) {
    $.get('/product/add-favorite/',{
    'jur75@4KDOUTDL[PWQIEYWK.BZN;A9YFEGFEIIY':Idproduct,
     }).then(
         res=>{
             return res
         }
    )
}
function Like(Id) {
    const likeIcon = document.getElementById('iconR-'+ Id);
    const likeIcon2 = document.getElementById('iconS-'+ Id);
    if (likeIcon.style.display === 'block'){
        likeIcon.style.display = 'none';
        likeIcon2.style.display = 'block';
    }
    else {
            likeIcon.style.display = 'block';
            likeIcon2.style.display = 'none';
    }
}
function Delete(Id) {
    const cart = document.getElementById('cart'+Id)
    cart.style.display = 'none';
}

function CommentJS(Id) {
    const commentText=$('#floatingTextarea2').val()
    const comment = document.getElementById('floatingTextarea2');
    const reply = document.getElementById('link-reply')
    if (commentText === ""){
        reply.addEventListener('click',function () {
        comment.scrollIntoView()
    })
    }else {
     $.get('/product/add-comment/',{
     'comment':commentText,
     'object_id':Id,
     }).then(
         res=>{
             $('#comment_list').html(res);
             Swal.fire({
                          title: "بازخورد با موفقیت ثبت شد!",
                          text: "بعد از تایید بازخورد شما نمایش داده می شود",
                          icon: "success",
                          confirmButtonText: "باشه"
                        });
         }
     )
    }


}
