

$(document).ready(function() {
    $('#to_toogle').hide();
    $("#add_restaurant").on('click', function () {
       $('#to_toogle') .toggle();
    });
});


let currentTab = 0;
showTab(currentTab);

function showTab(n) {
    let x = document.getElementsByClassName('tab');
    x[n].style.display = 'block';
    if (n == 0) {
        document.getElementById('prevBtn').style.display = 'none';
    }
    else {
        document.getElementById('prevBtn').style.display = 'inline';
    }
    if (n == (x.length -1)) {
        document.getElementById('nextBtn').innerHTML = 'Submit';
        document.getElementById('nextBtn').className = 'btn btn-success';
    }
    else {
        document.getElementById('nextBtn').innerHTML = 'Next';
        document.getElementById('nextBtn').className = 'btn btn-dark';
    }
};


function nextPrev(n) {
    let x = document.getElementsByClassName('tab');
    x[currentTab].style.display = 'none';
    currentTab = currentTab + n;
    if (currentTab >= x.length){
        document.getElementById('regForm').submit();
        return false;
    }
    showTab(currentTab);
};


