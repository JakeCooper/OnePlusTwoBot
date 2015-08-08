//get the response from this first

//get request to the html
//get the mail id
var https=require('https');

var apikey="Your Mailinator Api Key";
var oneplusId="Your one plus token";
x=function(){
	console.log('inside');
	https.get('https://www.mailinator.com', function(res) {
	var data;
	res.on('data', function(d) {
		data+=d;
	});
	res.on('end',function(da){
		var index=(data.indexOf("<a href='inbox.jsp?to="));
		var subst=data.substring(index);
		var slashIndex=subst.indexOf('</a>');
		var bslash=subst.indexOf('>');
		var mailId=(data.substring(index+bslash+1,index+bslash+slashIndex));
		mailId=mailId.replace('</a>','');
		mailId=mailId.split('</span>').join('');
		mailId=mailId.trim();
		var indexStr=mailId.indexOf('@mailinator.com');
		mailId=mailId.substring(0,indexStr)+'@mailinator.com';
		console.log(mailId);
		https.get("https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&email="+mailId+"&koid="+oneplusId,function(res1){
			 setTimeout(function () {
			https.get("https://api.mailinator.com/api/inbox?to=" + mailId + "&token="+apikey,function(res2){
				//console.log(res2);
				var data1='';
				res2.on('data', function(d) {
					data1+=d;
				});
				res2.on('end',function(da){
					data1=(JSON.parse(data1));
					var id=(data1.messages[data1.messages.length-1].id);


					
					https.get("https://api.mailinator.com/api/email?id="+id+"&token="+apikey,function(res3){
						
						var data1='';
						res3.on('data', function(d) {
							data1+=d;
						});
						res3.on('end',function(da){
							data1=(JSON.parse(data1));



							var content=data1.data.parts[0].body;
							var contIndex=content.indexOf('https:');
							var string_url=content.substring(contIndex,contIndex+68);
							https.get(string_url,function(res3){
								console.log('ended');
								x();
							});	


						});
					});

					});

				});

    }, 5000);


			});
		})
}).on('error', function(e) {
	console.error(e);
});
}
x();



//https://api.mailinator.com/api/inbox?to=hsdars@mailinator.com&token=203ea3b4ac404f70989f840c025b232f