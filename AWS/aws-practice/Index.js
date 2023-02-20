


$(document).ready(function() {
  $('#AddItems').click(function() {
    const id = $('#id').val();
    $('#id').val("");
    const price = $('#price').val();
    $('#price').val("");
    const name = $('#name').val();
    $('#name').val("");
    const qty = $('#qty').val();
    $('#qty').val("");
    let request = new XMLHttpRequest();
    let url="";
    if(id==""){
      return;
    }
    else{
      url = `	https://xbg1tvlta9.execute-api.us-west-1.amazonaws.com/items`;
    }
    console.log(id)
    console.log(url)
    request.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        // console.log(this.response)
        const response = JSON.parse(this.responseText);
        getElements(response,id);
      }
    };
    request.open("PUT", url, true);
    request.setRequestHeader("Content-Type", "application/json");
    // var data="id="+id+"&price="+price+"&name="+name;
    var data={"id":id,"name":name,"price":price,"qty":qty};
    data=JSON.stringify(data);
    console.log(data);
    request.send(data);

   function getElements(response,id) {
    
	  console.log(response)
    var temp = document.getElementById('container')
    let txt = "----------------------------------<br/>";
        txt=response['Message']+"<br/>";
      txt+="----------------------------------<br/>";
      temp.innerHTML=txt;
      console.log("done")
    }
  });


  $('#RemoveItems').click(function() {
    const id = $('#id').val();
    $('#id').val("");
    let request = new XMLHttpRequest();
    let url="";
    if(id==""){
      url = `	https://xbg1tvlta9.execute-api.us-west-1.amazonaws.com/items`;
      return;
    }
    else{
      url = `	https://xbg1tvlta9.execute-api.us-west-1.amazonaws.com/items/`+id;
    }
    
    console.log(id)
    console.log(url)
    request.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        console.log(this.response)
        const response = JSON.parse(this.responseText);
        getElements(response,id);
      }
    };

    request.open("DELETE", url, true);
    request.send();

   function getElements(response,id) {
    
	  console.log(response)
    var temp = document.getElementById('container')
    let txt = "----------------------------------<br/>";
        txt=response+"<br/>";
      txt+="----------------------------------<br/>";
      temp.innerHTML=txt;
      console.log("done")
    }
  });

  $('#GetItems').click(function() {
    const id = $('#id').val();
    $('#id').val("");
    let request = new XMLHttpRequest();
    let url="";
    if(id==""){
      url = `	https://xbg1tvlta9.execute-api.us-west-1.amazonaws.com/items`;
    }
    else{
      url = `	https://xbg1tvlta9.execute-api.us-west-1.amazonaws.com/items/`+id;
    }
    
    console.log(id)
    console.log(url)
    request.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        // console.log(this.response)
        const response = JSON.parse(this.responseText);
        getElements(response,id);
      }
    };

    request.open("GET", url, true);
    request.send();

   function getElements(response,id) {
    
	  console.log(response)
    var temp = document.getElementById('container')
    let txt = "----------------------------------<br/>";
    if(id==""){
      for (let x in response) {
        console.log(response[x]);
        for(y in response[x]){
          txt += y +": "+response[x][y]+"<br/>";
            // for(z in response[x][y])
            //   txt+= response[x][y]+ "<br/>"
        }
        txt+=    "----------------------------------<br/>"   ; 
      };
    }
    else{
      for (let x in response) {
        txt += x +": "+response[x]+"<br/>";
          // for(y in response[x])
          //   txt+= y+ "<br/>"        
      }; 
      txt+="----------------------------------<br/>";
    };
        temp.innerHTML=txt;
        console.log("done")
    }
  });
});