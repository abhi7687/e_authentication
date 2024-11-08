import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './OTPPage.css';
function OTPPage() {
  const navigate = useNavigate();
  const [otp, setOtp] = useState('');

  const handleInputChange = (e) => {
    setOtp(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate OTP validation
    if (otp === '123456') {
      console.log("OTP verified successfully");
      // Redirect to a success page (or main app page)
      navigate('/success');
    } else {
      console.log("Invalid OTP");
    }
  };

  return (
    <div>
      <h2>OTP Verification</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="otp"
          placeholder="Enter OTP"
          value={otp}
          onChange={handleInputChange}
        />
        <button type="submit">Verify OTP</button>
      </form>
    </div>
  );
}

export default OTPPage;
