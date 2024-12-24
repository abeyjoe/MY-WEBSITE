<?php
$matric = $_POST['matric'];
$fname = $_POST['fname'];
$lname = $_POST['lname'];
$gender = $_POST['gender'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$sor = $_POST['sor'];
$tnc = $_POST['tnc'];

//Database connection
$conn = new mysqli('localhost','root','','abeyjoe');
if($conn->connect_error){
    die('Connection Failed : '.$conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into signup(matric, fname, lname, gender, email, phone, sor, tnc) values(?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssiss", $matric, $fname, $lname, $gender, $email, $phone, $sor, $tnc);
    $stmt->execute();
    // echo "Registration Successfull.......";
    echo "<script>window.location.href = './index.html';</script>";
    $stmt->close();
    $conn->close();
}

?>