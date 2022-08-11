let soldEl = document.querySelectorAll('#sold')
let answerEl = document.querySelectorAll('#answered')
soldEl.forEach(soldEl => {
    if (soldEl.textContent == 'True') {
        soldEl.textContent = 'Status: Sold'
    }
    if (soldEl.textContent == 'False') {
        soldEl.textContent = 'Status: Available'
    }
})

answerEl.forEach(answerEl => {
    if (answerEl.textContent == 'True') {
        answerEl.textContent = 'Status: Answerd'
    }
    if (answerEl.textContent == 'False') {
        answerEl.textContent = 'Status: Not Answered'
    }
})


// ------------------------------------------------------------------------------------

// let replyEl = document.getElementById("reply")
// replyEl.addEventListener("click", function () {
//     replyEl.insertAdjacentHTML('afterend',
//         `<div class="content-section p-0">
//                             <form method="POST" enctype="multipart/form-data">
//                                 {% csrf_token %}
//                                 <fieldset class="form-group mb-0">
//                                     {{ comment_form|crispy}}
//                                 </fieldset>
//                                 <div class="form-group mb-2 d-flex justify-content-end">
//                                     <button class="btn btn-secondary btn-sm" type="submit">Comment</button>
//                                 </div>
//                             </form>
//                         </div> `)
// });





// function formExit() {
//     document.getElementById("newForm").remove();
//   }

//   function myFunction(id) {
//     if (document.contains(document.getElementById("newForm"))) {
//       document.getElementById("newForm").remove();
//     }

//     var d1 = document.getElementById(id);
//     d1.insertAdjacentHTML('afterend',
//       '<form id="newForm" class="form-insert py-2" method="post"> \
//                 <div class="d-flex justify-content-between"><h2>Reply:</h2><div><button type="button" class="btn btn-outline-secondary" onclick="formExit()"">Close</button></div></div> \
//                 <label for="id_name">Name:</label> \
//                 <input type="text" name="name" class="col-sm-12" maxlength="50" required="" id="id_name">\
//                 <select name="parent" class="d-none" id="id_parentt"> \
//                 <option value="' + id + '" selected="' + id + '"></option> \
//                 </select> \
//                 <label for="id_email">Email:</label> \
//                 <input type="text" name="email" class="col-sm-12" maxlength="254" required="" id="id_email"> \
//                 <label for="id_content">Content:</label> \
//                 <textarea name="content" cols="40" rows="5" class="form-control" required id="id_content"></textarea> \
//                 {% csrf_token %} \
//                 <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button> \
//               </form>');

//     //document.querySelector('#id_parentt [value="' + id + '"]').selected = true;
//   }

//   $('#myForm').trigger("reset");
