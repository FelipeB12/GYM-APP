<Dialog open={open} onClose={handleClose}>
<DialogTitle>Add New Appointment</DialogTitle>
<DialogContent>
  <TextField
    autoFocus
    margin="dense"
    name="client"
    label="Client Name"
    type="text"
    fullWidth
    value={newAppointment.client}
    onChange={handleInputChange}
  />
  <TextField
    margin="dense"
    name="date"
    label="Date"
    type="date"
    fullWidth
    InputLabelProps={{
      shrink: true,
    }}
    value={newAppointment.date}
    onChange={handleInputChange}
  />
  <TextField
    margin="dense"
    name="time"
    label="Time"
    type="time"
    fullWidth
    InputLabelProps={{
      shrink: true,
    }}
    value={newAppointment.time}
    onChange={handleInputChange}
  />
  <TextField
    margin="dense"
    name="purpose"
    label="Purpose"
    type="text"
    fullWidth
    value={newAppointment.purpose}
    onChange={handleInputChange}
  />
</DialogContent>
<DialogActions>
  <Button onClick={handleClose} color="primary">
    Cancel
  </Button>
  <Button onClick={handleAddAppointment} color="primary">
    Add
  </Button>
</DialogActions>
</Dialog>
</div>
);
}

export default AppointmentsPage;