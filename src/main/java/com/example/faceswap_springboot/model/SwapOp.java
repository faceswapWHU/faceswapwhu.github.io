package com.example.faceswap_springboot.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "operations")
public class SwapOp {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private int uid;

    @Column(nullable = false, unique = true)
    private String src;

    @Column(nullable = false, unique = true)
    private String tar;

    @Column(nullable = false, unique = true)
    private String res;

    @Column(name = "create_at", nullable = false, updatable = false)
    private LocalDateTime createdAt = LocalDateTime.now();

    @Column(nullable = false)
    private LocalDateTime finish_at;

    @Column(nullable = false)
    private int isfinish;

    // Getters and setters

}
