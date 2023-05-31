
import { Formik, Field, Form, ErrorMessage, useFormik } from "formik";
import * as Yup from "yup";
import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

function ForgetPassword() {
    const navigate=useNavigate()
    const initialvalues = {
        email: "",
        password: ""
    }
    const [responseData,setResponseData]=useState({
        responseText:"",
        responseClass:""
    })


    const validationschema = Yup.object({
        password: Yup.string().required("Password is required!")
    })


    function onSubmit(values,{resetForm}){
        axios.put("http://127.0.0.1:8000/api/users/resetpassword",values)
        .then((response)=>{
            setResponseData({
                responseText:"Successfully Changed",
                responseClass:"alert alert-success"
            });
            setTimeout(()=>{
                navigate("/login")
            },1000)
            
        },
        (error)=>{
            setResponseData({
                responseText:"Invalid Username or Password!!",
                responseClass:"alert alert-danger"
            });

        })
        .catch((error)=>{
            console.log(error)
        })
        resetForm()

    }
    return (


        <div className="container">
            <div className="row">
                <div className="col-md-3"></div>
                <div className="col-md-6">
                    <div style={{ background: "#fff", padding: "30px 40px", borderRadius: "10 px", marginTop: "80px" }}>
                        <h1>Reset Password</h1>
                        <div className={responseData.responseClass} role="alert">{responseData.responseText}</div>
                        <hr />
                        <Formik initialValues={initialvalues} validationSchema={validationschema} validateOnMount onSubmit={onSubmit}>
                            {(formik) => {
                                return (
                                    <Form>
                                        <div className="form-group">
                                            <label htmlFor="email">E-Mail</label>
                                            <Field type="email" name="email" className="form-control" />
                                            {/* <ErrorMessage name="email">
                                                {(errormessage) => (<small className="text-danger">{errormessage}</small>)}
                                            </ErrorMessage> */}
                                        </div>

                                        <div className="form-group">
                                            <label htmlFor="password">New Password</label>
                                            <Field name="password" type="password" className="form-control" />
                                            <ErrorMessage name="password">{(errormessage) => (<small className="text-danger">{errormessage}</small>)}</ErrorMessage>
                                        </div>
                                        <input type="submit" value="Login" disabled={!formik.isValid} />
                                        <a href="/login">Cancel</a>
                                    </Form>
                                )
                            }}

                        </Formik>


                    </div>
                </div>
                <div className="col-md-3"></div>
            </div>
        </div>








    )

}


export default ForgetPassword;