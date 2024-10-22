package com.example.faceswap_springboot.controller;

import com.example.faceswap_springboot.dto.UserLoginDto;
import com.example.faceswap_springboot.dto.UserRegistrationDto;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.Collections;

@RestController
@RequestMapping("/api/swap")
@CrossOrigin(origins = "http://localhost:3000")
public class SwapController {
    @PostMapping("/img")
    public ResponseEntity<?> swapImg(@RequestBody UserRegistrationDto userDto) {
        try {

            return ResponseEntity.ok(Collections.singletonMap("message", "User registered in successfully"));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(Collections.singletonMap("error", e.getMessage()));
        }
    }

    @PostMapping("/video")
    public ResponseEntity<?> swapVideo(@RequestBody UserLoginDto userLoginDto) {
        try {

            return ResponseEntity.ok(Collections.singletonMap("message", "User logged in successfully"));
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(Collections.singletonMap("error", e.getMessage()));
        }
    }
}
