package com.example.faceswap_springboot.controller;

import com.example.faceswap_springboot.dto.UserLoginDto;
import com.example.faceswap_springboot.dto.UserRegistrationDto;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;
import com.example.faceswap_springboot.service.UserService;

@RestController
@RequestMapping("/api/auth")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    /*
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securePassword123"
    * */
    @PostMapping("/register")
    public ResponseEntity<?> registerUser(@RequestBody UserRegistrationDto userDto) {
        try {
            userService.registerUser(userDto.getUsername(), userDto.getEmail(), userDto.getPassword());
            return ResponseEntity.ok("User registered successfully");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping("/login")
    public ResponseEntity<?> loginUser(@RequestBody UserLoginDto userLoginDto) {
        try {
            userService.loginUser(userLoginDto.getUsernameOrEmail(), userLoginDto.getPassword());
            System.out.println("login user: " + SecurityContextHolder.getContext().getAuthentication().getName());
            return ResponseEntity.ok("User logged in successfully");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(e.getMessage());
        }
    }
}
