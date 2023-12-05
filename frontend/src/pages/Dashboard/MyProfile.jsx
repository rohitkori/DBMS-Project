import React from "react";
import Requests from "../../components/Requests";
import MyInfo from "../../components/MyInfo";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import "./MyProfile.css";
import Divider from "@mui/material/Divider";

const MyProfile = () => {
  return (
    <div className="myprofile-main">
      <div className="myprofile-about">
        <h1>MY PROFILE</h1>
        <p>DONOR</p>
        <MyInfo />
      </div>
      <Divider
        variant="middle"
        sx={{ marginBottom: "20px", marginTop: "20px" }}
      />
      <div className="all-requestes-main">
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <h2>ALL REQUESTS</h2>
          <Button>Create New</Button>
        </Box>
        <Requests />
      </div>
    </div>
  );
};

export default MyProfile;
