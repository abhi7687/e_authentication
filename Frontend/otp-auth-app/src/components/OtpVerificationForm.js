// src/components/OtpVerificationForm.js
import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import api from '../Api';
import { useNavigate, useLocation } from 'react-router-dom';

const OtpVerificationForm = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { email } = location.state || {};

  const initialValues = {
    otp: '',
  };

  const validationSchema = Yup.object({
    otp: Yup.string().length(6, 'OTP must be 6 digits').required('OTP is required'),
  });

  const handleSubmit = async (values) => {
    try {
      const response = await api.post('/verify-otp', { email, otp: values.otp });
      if (response.data.message === 'OTP verified successfully, login complete') {
        navigate('/dashboard'); // Redirect to a protected page like a dashboard
      }
    } catch (error) {
      console.error('OTP verification failed:', error.response?.data?.detail);
      alert('OTP verification failed. Try again.');
    }
  };

  return (
    <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
      <Form>
        <div>
          <label>OTP:</label>
          <Field name="otp" type="text" />
          <ErrorMessage name="otp" component="div" />
        </div>
        <button type="submit">Verify OTP</button>
      </Form>
    </Formik>
  );
};

export default OtpVerificationForm;
