import React, {useState, useEffect} from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import ImageIcon from "@mui/icons-material/Image";
import Card from "@mui/material/Card";
import Divider from "@mui/material/Divider";
import Button from "@mui/material/Button";
import { Box } from "@mui/material";
import useAxios from "../utils/useAxios";

const Requests = () => {
  const [requests, setRequests] = useState([]); // [
  
  const api = useAxios();
  // const requests = [
  //   {
  //     request_id: 1,
  //     type: "food pick up",
  //     address: "1234 Main St",
  //   },
  //   {
  //     request_id: 2,
  //     type: "food pick up",
  //     address: "1234 Main St",
  //   },
  //   {
  //     request_id: 3,
  //     type: "food pick up",
  //     address: "1234 Main St",
  //   },
  //   {
  //     request_id: 4,
  //     type: "food pick up",
  //     address: "1234 Main St",
  //   },
  // ];
  useEffect(() => {
    const fetchOpenPickups = async () => {
      const response = await api.get("/open-pickups/");
      if (response.status === 200) {
        setRequests(response.data["Requests"]);
      }
      console.log(response.data);
    }
    fetchOpenPickups();

  }, []);

  return (
    <div>
      <List
        sx={{
          width: "600px",
          maxWidth: 600,
          bgcolor: "background.paper",
        }}
      >
        
        {requests.map((request) => (
          <Card>
            <ListItem
              secondaryAction={
                <Box>
                  <Button key="accept" sx={{ color: "green" }}>
                    accept
                  </Button>
                  <Button key="reject" sx={{ color: "red" }}>
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
            <Divider variant="inset" component="li" />
          </Card>
        ))}
      </List>
    </div>
  );
};

export default Requests;
