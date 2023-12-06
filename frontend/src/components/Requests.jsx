import React, {useState, useEffect} from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import ImageIcon from "@mui/icons-material/Image";
import Card from "@mui/material/Card";
import toast from "react-hot-toast";
import Button from "@mui/material/Button";
import { Box } from "@mui/material";
import useAxios from "../utils/useAxios";

const request = [
  {
    request_id: 1,
    type: "food pick up",
    address: "1234 Main St",
  },
  {
    request_id: 2,
    type: "food pick up",
    address: "1234 Main St",
  },
  {
    request_id: 3,
    type: "food pick up",
    address: "1234 Main St",
  },
  {
    request_id: 4,
    type: "food pick up",
    address: "1234 Main St",
  },
];
const Requests = () => {
  const [acceptedRequests, setAcceptedRequests] = React.useState([]);
  const [requests, setRequests] = React.useState(request);

  function handleRequest(e, status) {
    if (status) {
      toast.success("Request accepted");
      console.log(e);
      setAcceptedRequests([...acceptedRequests, e]);
      setRequests(
        requests.filter((request) => request.request_id !== e.request_id)
      );
    } else {
      toast.error("Request rejected");
      setRequests(
        requests.filter((request) => request.request_id !== e.request_id)
      );
    }
  }

  return (
    <div>
      <List
        sx={{
          width: "600px",
          maxWidth: 600,
          // bgcolor: "background.paper",
        }}
      >
        
        {requests.map((request) => (
          <Card
            sx={{
              width: "600px",
              maxWidth: 600,
              bgcolor: "background.paper",
              marginBottom: "10px",
            }}
          >
            <ListItem
              secondaryAction={
                <Box>
                  <Button
                    onClick={() => handleRequest(request, true)}
                    key="accept"
                    sx={{ color: "green" }}
                  >
                    accept
                  </Button>
                  <Button
                    onClick={() => handleRequest(request, false)}
                    key="reject"
                    sx={{ color: "red" }}
                  >
                    reject
                  </Button>
                </Box>
              }
            >
              <ListItemAvatar>
                <Avatar>
                  <ImageIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText
                primary="name"
                secondary={request.pickup_address}
              />
            </ListItem>
          </Card>
        ))}
        <h2>Accepted Requests</h2>
        {acceptedRequests.map((request) => (
          <Card
            sx={{
              width: "600px",
              maxWidth: 600,
              bgcolor: "background.paper",
              marginBottom: "10px",
            }}
          >
            <ListItem
              secondaryAction={
                <Box>
                  <Button sx={{ color: "green" }}>accepted</Button>
                </Box>
              }
            >
              <ListItemAvatar>
                <Avatar>
                  <ImageIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText
                primary={request.type}
                secondary={request.address}
              />
            </ListItem>
          </Card>
        ))}
      </List>
    </div>
  );
};

export default Requests;
