
<!DOCTYPE html>
<html lang="en">
<head>
    <title>ACA | IT Project Management</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="description" content="Learn IT Project Management">
    <meta name="keywords" content="course, academy, it, Project, Management">
    <meta name="author" content="Armenian Code Academy">
    <meta property="og:image" content="http://aca.am/assets/img/itpm/itpm_fb.png"/>

    <!-- favicons -->
    <link rel="apple-touch-icon" sizes="57x57" href="../assets//favicons/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="../assets/favicons/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../assets/favicons/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="../assets/favicons/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../assets/favicons/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="../assets/favicons/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="../assets/favicons/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="../assets/favicons/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../assets/favicons/apple-touch-icon-180x180.png">
    <link rel="icon" type="image/png" href="../assets/favicons/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="../assets/favicons/favicon-194x194.png" sizes="194x194">
    <link rel="icon" type="image/png" href="../assets/favicons/favicon-96x96.png" sizes="96x96">
    <link rel="icon" type="image/png" href="../assets/favicons/android-chrome-192x192.png" sizes="192x192">
    <link rel="icon" type="image/png" href="../assets/favicons/favicon-16x16.png" sizes="16x16">
    <link rel="manifest" href="../assets/favicons/manifest.json">
    <meta name="msapplication-TileColor" content="#73afb6">
    <meta name="msapplication-TileImage" content="../assets/favicons/mstile-144x144.png">
    <meta name="theme-color" content="#ffffff">
    <!-- /favicons -->

    <!-- Bootstrap core CSS -->
    <link href="../assets/css/bootstrap.css" rel="stylesheet">
    <link href="../assets/css/scrolling-nav.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../assets/css/main.css" rel="stylesheet">
    <link href="../assets/css/courses.css" rel="stylesheet">
    <link href="../assets/css/courses_itpm.css?v=1.1" rel="stylesheet">

    <!-- ICONS -->
    <link href="../assets/css/font-awesome.min.css" rel="stylesheet">
    <link href="../assets/css/flag-icon.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../assets/css/flaticon.css">
    <style>
        [class^="flaticon-"]:before,
        [class*=" flaticon-"]:before,
        [class^="flaticon-"]:after,
        [class*=" flaticon-"]:after {
            font-family: Flaticon;
            font-size: 100px;
            color: #049CB4;;
        }
        #education .container div:nth-child(3):hover i:before,
        #education .container div:nth-child(3):hover i:after,
        #education .container div:nth-child(4):hover i:before,
        #education .container div:nth-child(4):hover i:after,
        #education .container div:nth-child(5):hover i:before,
        #education .container div:nth-child(5):hover i:after {
            color: #f2f2f2;
        }
        #project {
            background-size: cover !important;
        }
        #project i:before{
            color: white;
        },
        #project i:after {
            font-family: Flaticon;
            font-size: 150px;
            color: #000000;
        }
        .alert {
            font-size: 16px !important;
            line-height: 1.7;
            color: #000000
        }
        @media (max-width: 768px) {
            #project i:before,
            #project i:after {
                font-size: 50px;
            }
        }

    </style>


    <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Raleway:400,300,700' rel='stylesheet' type='text/css'>

    <script src="../assets/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <script src="../assets/js/initTelephoneInputs.js"></script>
	<nav class="menu" id="theMenu">
		<a href="index.html#courses"><div id="backButton"><i class="glyphicon glyphicon-chevron-left"></i></div></a>
	</nav>

    <div id="enrollbox" class="modal fade" role="dialog">
        <div class="modal-dialog modal-steps">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 container-step="1" class="js-title-step" >
                        <span class="label label-success">1</span>
                        Application guideline
                    </h4>
                    <h4 container-step="2" class="js-title-step hide" >
                        <span class="label label-success">2</span>
                        Application Form
                    </h4>
                    <h4 container-step="3" class="js-title-step hide" >
                        <span class="label label-success">3</span>
                        Your application has been submitted!
                    </h4>
                </div>
                <div class="modal-body">
                    <div class="row" container-step="1">
                        <div class="jumbotron jumb-costum">
                            <div class="row">
                                <img class="hidden-xs" src="../assets/img/enroll-steps/steps-for-enroll-en.png" width="100%">
                                <img class="hidden-sm hidden-md hidden-lg" src="../assets/img/enroll-steps/steps-for-enroll-mobile-en.jpg" width="100%">
                                <div class="col-xs-12">
                                    <label class="conditions">
                                        <input id="agree" type="checkbox" name="agree" value="agree" />I have read and agree to the application guidelines.
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row hide" container-step="2">
                        <div class="jumbotron jumb-costum">
                            <div class="row">
                                <div class="col-xs-12">
                                    <form class="form">
                                        <input type="hidden" name="courseName" value="IT Project Management" /><input type="hidden" name="courseID" value="2000" />
                                        <input type="hidden" name="courseLevel" value="1" />
                                        <input type="hidden" name="courseStarts" value="[for November 2019]" />
                                        <div class="form-group">
                                            <input id="applicantName" type="text" name="applicantName" class="form-control" placeholder="First and last names" required autofocus>
                                        </div>
                                        <div class="form-group">
                                            <input id="applicantEmail" type="email" name="applicantEmail" class="form-control" placeholder="Email" required>
                                        </div>
                                        <div class="form-group">
                                            <input id="applicantPhone" type="tel" name="applicantPhone" class="form-control bfh-phone" data-format="ddd dd dd dd">
                                        </div>
                                        <div class="form-group" style="display: none;">
                                            <select name="preferredTime" class="form-group form-control" id="preferredTime">
                                                <option selected value="Evening">After 18:00</option>
                                            </select>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row hide" container-step="3" data-title="Հայտը ընդունված է">
                        <div class="jumbotron jumb-costum">
                            <p class="enroll-labels">
                                Thank you for application! We have sent you an email explaining the enrollment process. Please check your email.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="modal-footer modal-footer-costum">
                    <button class="btn btn-success js-btn-step" data-step="1" disabled="disabled">
                        <span container-step="1" class="">Next</span>
                        <span container-step="2"class="hide">Submit</span>
                        <span container-step="3" class="hide">Close</span>
                    </button>
                </div>
            </div>
        </div>
    </div>


    <div id="header" class="jumbotron">
        <div class="container">
            <div class="row" id="langs" style="padding:0px;margin:0px;">
                <div class="col-xs-12">
<!--                    <a href="../hy/cpp.html"><span class="flag-icon flag-icon-am"></span></a>-->
<!--                            &nbsp;&nbsp;-->
<!--                    <a href="../en/cpp.html" class="active"><span class="flag-icon flag-icon-gb"></span></a>-->
                    <br>
                </div>
            </div>
            <div class="row">
                <div class="col-md-2 col-xs-2 text-center hidden-xs">
                    <img src="../assets/img/intro-level/itpm-logo.png" alter="courseImage">
                </div>
                <div class="col-md-6 col-sm-10 col-xs-12 title-header">
                    <h1>IT Project Management </h1>
                </div>
                <div class="col-md-4 col-xs-12 text-center info-header">
					<div id="iosThanks" class="thanks-for-subscription ">
                        <h4>Enrollment is open</h4>
                        <p><a class="btn btn-primary btn-lg btn-block btn-enroll" data-toggle="modal" data-target="#enrollbox" role="button">Enroll Now</a></p>
					</div>
                    <hr>
                    <h4>P: +374 (12) 48-16-32</h4>
                    <h4>E: info@aca.am</h4>
                </div>
            </div>
        </div>
    </div>
<!--
    <div class="container" id="langs">
        <div class="row">
            <div class="col-xs-12">
                <a href="../hy/web.html"><span class="flag-icon flag-icon-am"></span></a>
                        &nbsp;&nbsp;
                <a href="../en/web.html" class="active"><span class="flag-icon flag-icon-gb"></span></a>
            </div>
        </div>
    </div>
-->

    <div id="content">
        <div class="container">
            <div class="row row-offcanvas row-offcanvas-right">
                <div class="col-xs-12 col-sm-9">
<!--
                    <p class="pull-right visible-xs">
                        <button type="button" class="btn btn-primary btn-md btn-dark" data-toggle="offcanvas">Details &nbsp;<span class="glyphicon glyphicon-plus" aria-hidden="true"></span></button>
                    </p>
-->
                    <!--<nav class="pull-right visible-xs menu" id="viewMore">-->
                        <!--<div id="viewButton" data-toggle="offcanvas"><i class="fa fa-bars"></i></div>-->
                    <!--</nav>-->
                    <div id="about" class="jumbotron">
                        <div class="container">
                            <div class="row">
<!--
                                <div id="video" class="col-sm-5 col-xs-12">
                                    <div id="player"></div>
                                </div>
                                <div id="tutors" class="col-sm-offset-1 col-sm-6 col-xs-12">
-->
                                <div id="tutors" class="col-xs-12">
                                    <div class="container">
                                        <div class="col-xs-612">
                                            <div class="row">
                                                <div class="col-xs-12">
                                                    <img class="img-circle img-thumbnail" src="../assets/img/tutors/pm_anna_muradyan.jpeg" alt="tutor1">
                                                </div>
                                                <div class="col-xs-12">
                                                    <h3>Anna Muradyan</h3>
                                                    <strong><p>Catches</p></strong>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-xs-12">
                                    <h3>About the course</h3>
                                    <p>
This course has an aim to train and advance your knowledge in Project Management. With theoretical knowledge combined with practical skills and methods, you will learn the best Agile project management practices. The goal of the course is to give enough knowledge to kickstart or advance your career in project management. With the help of our experienced instructor, you will deepen your understanding of Agile software development, better understand how to run projects with Scrum, and get familiar with best case studies. Students will finish the course by conducting their own case studies. 
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                 <div class="row">
                                 <div id="final" class="col-xs-12">
                            <div class="container">
                                <div class="row">
                                    <div class="col-xs-12">
                                        <h2>Group Project</h2>
                                    </div>
                                    <div class="col-xs-2 text-center">
                                        <i class="glyphicon glyphicon-briefcase"></i>
                                    </div>
                                    <div class="col-xs-10">
                                        <p>The goal of the course is to give knowledge and indispensable practice, which will become a base to help students to finish the course by conducting a case study. Working in groups does not only contribute to a better understanding of the course material but also creates a space for discussion and collaboration as a result of which students can find solutions to more complex problems.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    <div class="row">
                        <div id="education" class="col-xs-12">
                            <div class="container">
                                <div class="header1 col-xs-12">
                                    <h1>Learning Process</h1><br>
                                </div>
                                <div class="header1 col-xs-12">
                                    <p>The topics will be covered in a diversified but logically structured order to make the learning process as efficient as possible. Most topics in the course are accompanied by case studies intended for both in-class and homework assignments.</p>
                                </div>
                                <div class="col-sm-4 col-xs-12">
                                    <h3>Lectures</h3>
                                    <i class="flaticon-instructor"></i>
                                </div>
                                <div class="col-sm-4 col-xs-12">
                                    <h3>Seminars</h3>
                                    <i class="flaticon-programming9"></i>
                                </div>
                                <div class="col-sm-4 col-xs-12">
                                    <h3>Homework</h3>
                                    <i class="flaticon-task2"></i>
                                </div>
                            </div>
                        </div>
<!--                        <div id="project" class="col-xs-12">-->
<!--                            <div class="container">-->
<!--                                -->
<!--                            </div>-->
<!--                        </div>-->
                        <div id="final" class="col-xs-12">
                            <div class="container">
                                <div class="row">
                                    <div class="col-xs-12">
                                        <h2>Get Qualified</h2>
                                    </div>
                                    <div class="col-xs-2 text-center">
                                        <i class="glyphicon glyphicon-certificate"></i>
                                    </div>
                                    <div class="col-xs-10">
                                        <p>The status of graduate of this course will allow you to continue your studies on a deeper level.</p>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-xs-12">
                                        <h2>Gain practical knowledge</h2>
                                    </div>
                                    <div class="col-xs-10">
                                        <p>Students passing this course should display knowledge, ability, and behavioral skills to manage projects at an entry/mid-level in the IT industry, as well as familiarity with concepts, tools, techniques, and methodologies used.</p>
                                    </div>
                                    <div class="col-xs-2 text-center">
                                        <i class="glyphicon glyphicon-check"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="enroll" class="col-xs-12" style="text-align: center;">
                            <div class="row">
                                <div class="col-sm-4 col-sm-offset-4 col-xs-8 col-xs-offset-2 text-center">
									<div id="iosThanks" class="thanks-for-subscription">
                                        <h4>Enrollment is open</h4>
										<p><a class="btn btn-block btn-lg btn-enroll" data-toggle="modal" data-target="#enrollbox" role="button">Enroll Now</a></p>
									</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-xs-12 col-sm-3" id="sidebar">
                    <div class="list-group">
                        <div class="col-xs-12" id="details">
                            <table class="table">
                                <tr>
                                    <td class="hidden-sm hidden-xs"><i class="fa fa-calendar-check-o"></i></td>
                                    <td>Duration:</td>
                                    <td>3 months</td>
                                </tr>
                                <tr>
                                    <td class="hidden-sm hidden-xs"><i class="fa fa-hourglass-end"></i></td>
                                    <td>Effort:</td>
                                    <td>4 hours/week</td>
                                </tr>
                                <tr>
                                    <td class="hidden-sm hidden-xs"><i class="fa fa-tags"></i></td>
                                    <td>Price:</td>
                                    <td>49000 AMD/month</td>
                                </tr>
                                <tr>
                                    <td class="hidden-sm hidden-xs"><i class="fa fa-line-chart"></i></td>
                                    <td>Level:</td>
                                    <td>Intermediate</td>
                                </tr>
                            </table>
                        </div>
                        <div class="col-xs-12" id="syllabus">
                            <div class="list-group">
                                <h2>Course Syllabus</h2>
                                <table class="table table-condensed">
                                    <tr>
                                        <td>Overview of Agile Project Management</td>
                                    </tr>
                                    <tr>
                                        <td>Agile Components</td>
                                    </tr>
                                    <tr>
                                        <td>Overview of Scrum
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>Running projects with Scrum</td>
                                    </tr>
                                    <tr>
                                        <td>Overview of Kanban</td>
                                    </tr>
                                    <tr>
                                        <td>Agile design</td>
                                    </tr>
                                    <tr>
                                        <td>Agile software development</td>
                                    </tr>
                                    <tr>
                                        <td>Agile teams</td>
                                    </tr>
                                    <tr>
                                        <td>Agile at scale</td>
                                    </tr>
                                    <tr>
                                        <td>Project Management tools</td>
                                    </tr>
                                    <tr>
                                        <td>Jira/Confluence/Asana/Trello </td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                        <div class="col-xs-12" id="timeline">
                            <div class="list-group">
                                <h2>Timeline</h2>
                                <hr>
                                <ul>
                                    <li>
                                        <h3>Assesment</h3>
                                    </li>
                                    <li>
                                        <h3>Lectures &amp; Seminars</h3>
                                    </li>
                                    <li>
                                        <h3>Final Project</h3>
                                    </li>
                                    <li>
                                        <h3>Exam &amp; Certificate</h3>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-xs-12" id="discounts">
                            <div>
                                <h2>Discounts</h2>
                                <ul class="list-group">
                                    <li class="list-group-item">
                                        Best students will receive financial compensation depending on their performances.
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-xs-12" id="more">
                            <div class="list-group">
                                <h2>More Courses</h2>
                                <div class="list-group">
                                    <div class="list-group-item">
    <a href="intro-js.html">
        <p><img class="img-circle" src="../assets/img/intro-level/js.png" alter="item1">Introduction to JS</p>
    </a>
</div>
<div class="list-group-item">
    <a href="intro-java.html">
        <p><img class="img-circle" src="../assets/img/intro-level/java.png" alter="item1">Introduction to Java</p>
    </a>
</div>
<div class="list-group-item">
    <a href="intro-ios.html">
        <p><img class="img-circle" src="../assets/img/intro-level/ios.png" alter="item1">Fundamentals of iOS</p>
    </a>
</div>
<div class="list-group-item">
    <a href="qe-fundamentals.html">
        <p><img class="img-circle" src="../assets/img/intro-level/qa.png" alter="item2">Fundamentals of QA</p>
    </a>
</div>
<div class="list-group-item">
    <a href="intro-python.html">
        <p><img class="img-circle" src="../assets/img/intro-level/python.png" alter="item1">Introduction to Python</p>
    </a>
</div>
<div class="list-group-item">
    <a href="intro-cpp.html">
        <p><img class="img-circle" src="../assets/img/intro-level/cpp.png" alter="item1">Introduction to C++</p>
    </a>
</div>
<div class="list-group-item">
    <a href="intro-ui-ux.html">
        <p><img class="img-circle" src="../assets/img/intro-level/ui-ux.png" alter="item1">Fundamentals of UI/UX</p>
    </a>
</div>
<div class="list-group-item">
    <a href="../en/intro-it-pm.html">
        <p><img class="img-circle" src="../assets/img/intro-level/itpm.png" alter="item1">Intro to IT Project Mgmt.</p>
    <a href="../en/intro-it-pm.html">
</div>                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="../assets/js/bootstrap.min.js"></script>
    <script src="../assets/js/main.js"></script>
    <script src="../assets/js/bootstrap-formhelpers-phone.js"></script>
    <script src="../assets/js/jquery.easing.min.js"></script>
    <script src="../assets/js/scrolling-nav.js"></script>
    <script src="../assets/js/applicationStepsEn.js"></script>
    	<!-- Yandex.Metrika counter -->
	<script type="text/javascript">
        (function (d, w, c) {
            (w[c] = w[c] || []).push(function() {
                try {
                    w.yaCounter32334895 = new Ya.Metrika({
                        id:32334895,
                        clickmap:true,
                        trackLinks:true,
                        accurateTrackBounce:true,
                        webvisor:true
                    });
                } catch(e) { }
            });

            var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
            s.type = "text/javascript";
            s.async = true;
            s.src = "https://mc.yandex.ru/metrika/watch.js";

            if (w.opera == "[object Opera]") {
                d.addEventListener("DOMContentLoaded", f, false);
            } else { f(); }
        })(document, window, "yandex_metrika_callbacks");
	</script>
    <noscript><div><img src="https://mc.yandex.ru/watch/32334895" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
	<!-- /Yandex.Metrika counter -->
	</body>
	</html>