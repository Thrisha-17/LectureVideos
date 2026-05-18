package com.example.lecturenotes;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class NotesController {

@PostMapping("/save")
public String saveNotes(@RequestBody String notes) {

return "Notes Saved Successfully";
}
}
