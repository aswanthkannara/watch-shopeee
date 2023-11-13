def pay():
    if True:
        pass
    
    
    '''<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
    <script>
      $(document).ready(function() {
        $('#rzp-button1').click(function (e) { 
          var address = $('#address').val()
          var payment = "Razorpay"
          var token = $("input[name='csrfmiddlewaretoken']").val()
          e.preventDefault();
          console.log("innnn")
          $.ajax({
                type: "GET",
                url: "/razorpay",
                success: function (response) {
                    var options={
                        "key": "key_id", // Enter the Key ID generated from the Dashboard
                        //"amount": response.total*100,//response.total, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "amount": '{{grand_total}}'*100,
                        "currency": "INR",
                        "name": "cart",
                        "description": "Thank you for shopping with us",
                        {% comment %} "image": "https://example.com/your_logo", {% endcomment %}
                        // "order_id": response.id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response){
                            // alert(response.razorpay_payment_id);
                            data = {
                                "id": response.razorpay_payment_id,
                                "address" : address,
                                "payment" : payment,
                                'csrfmiddlewaretoken': token
                            }
                            $.ajax({
                                type: "POST",
                                url: "/checkout",
                                data: data,
                                success: function (response) {
                                  console.log(response)
                                  swal({
                                    title: "Payment Successful",
                                    text: "Your payment is successful",
                                    icon: "success",
                                    button: "OK",
                                  }).then(function() {
                                    window.location.href = "order_placed";
                                  });
                                }
                            });
                        },
                        "prefill": {
                            "name": "Gaurav Kumar",
                            "email": "",
                            "contact": "9999999999",
                        },
                        "notes": {
                            "address": "Razorpay Corporate Office"
                        },
                        "theme": {
                            "color": "#3399cc"
                        },
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });
        });
    });
    </script>'''