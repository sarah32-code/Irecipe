/**
 * Created by asazegar on 3/9/2017.
 */

function authenticate() {
    var user = $("#uname").val();
    var passwd = $('#passwd').val();

    var isValid=false;
    var authUser;

    $.each(users,function(k,v){
        if(v.email.trim()==user.trim() &&
            v.passwd == passwd){
            authUser = v;
            isValid=true;
        }
    });

    if(isValid){
        //set cookie
        var isAdmin = (authUser.gid==200)? true:false;
        var userInfo = {"uid":authUser.uid,"isAdmin":isAdmin};
        $.cookie("userInfo", userInfo);
        window.location.href="home.html";
    }else{
        logout();
        $('#messageBox').html('Invalid username or password. Please Try again!');
        $("#uname").val('');
        $('#passwd').val('');
    }
}

function isUserAuthenticated(isSecurePage,isAdminPage){

    var userInfo = $.cookie("userInfo");
    var ret=false;

    if(!userInfo){
        return ret;
    }
    userInfo = $.parseJSON(userInfo);

    if(isAdminPage && isSecurePage && userInfo && userInfo.uid){
        if(userInfo.isAdmin){
            ret=true;
        }
    }else if(isSecurePage && userInfo && userInfo.uid){
        ret=true;
    }

    return ret;
}



function logout(){
    $.removeCookie("userInfo");
}