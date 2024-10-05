package com.example.faceswap_springboot.service;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;
import com.example.faceswap_springboot.repository.UserRepository;
import com.example.faceswap_springboot.model.User;

@Service
public class UserService {
    private final AuthenticationManager authenticationManager;
    private final UserDetailsService userDetailsService;  // 用于加载用户详情
    private final UserRepository userRepository;
    private final PasswordService passwordService;

    public UserService(AuthenticationManager authenticationManager, UserDetailsService userDetailsService, UserRepository userRepository, PasswordService passwordService) {
        this.authenticationManager = authenticationManager;
        this.userDetailsService = userDetailsService;
        this.userRepository = userRepository;
        this.passwordService = passwordService;
    }

    public User registerUser(String username, String email, String rawPassword) throws Exception {
        // 检查用户名和邮箱是否已存在
        if (userRepository.findByUsername(username).isPresent()) {
            throw new Exception("Username already exists");
        }
        if (userRepository.findByEmail(email).isPresent()) {
            throw new Exception("Email already exists");
        }

        // 加密密码
        String encodedPassword = passwordService.encodePassword(rawPassword);

        // 创建并保存用户
        User newUser = new User();
        newUser.setUsername(username);
        newUser.setEmail(email);
        newUser.setPassword(encodedPassword);

        return userRepository.save(newUser);
    }

    public void loginUser(String usernameOrEmail, String password) {
        try {
            // 使用用户名或电子邮件进行认证
            Authentication authentication = authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(usernameOrEmail, password)
            );
            // 如果认证成功，设置认证信息到安全上下文中
            SecurityContextHolder.getContext().setAuthentication(authentication);
            System.out.println("login user: " + SecurityContextHolder.getContext().getAuthentication().getName());
        } catch (Exception e) {
            throw new RuntimeException("Invalid login credentials");
        }
    }
}