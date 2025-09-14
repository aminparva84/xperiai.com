// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}));

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar background change on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = document.querySelectorAll('.service-card, .stat-item, .contact-item');
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Email sending function
function sendEmail(event) {
    event.preventDefault();
    
    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    
    // Basic validation
    if (!name || !email || !subject || !message) {
        showNotification('Please fill in all fields', 'error');
        return;
    }
    
    if (!isValidEmail(email)) {
        showNotification('Please enter a valid email address', 'error');
        return;
    }
    
    // Create email content
    const emailBody = `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`;
    
    // Create mailto link
    const mailtoLink = `mailto:info@xperiai.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
    
    // Open email client
    window.location.href = mailtoLink;
    
    // Show success message
    showNotification('Opening your email client...', 'success');
    
    // Reset form after a short delay
    setTimeout(() => {
        document.getElementById('contactForm').reset();
    }, 1000);
}

// Email validation function
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style the notification
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#48bb78' : type === 'error' ? '#f56565' : '#4299e1'};
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
        font-weight: 500;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 300);
    }, 5000);
}

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroVisual = document.querySelector('.ai-visualization');
    
    if (heroVisual) {
        const rate = scrolled * -0.5;
        heroVisual.style.transform = `translateY(${rate}px)`;
    }
});

// Counter animation for statistics
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.textContent.replace(/\D/g, ''));
        const suffix = counter.textContent.replace(/\d/g, '');
        let current = 0;
        const increment = target / 50;
        
        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.ceil(current) + suffix;
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target + suffix;
            }
        };
        
        updateCounter();
    });
}

// Trigger counter animation when stats section is visible
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const statsSection = document.querySelector('.about-stats');
if (statsSection) {
    statsObserver.observe(statsSection);
}

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Add hover effects to service cards
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-10px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) scale(1)';
    });
});

// Add click effect to buttons
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        `;
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Interactive Neural Network with Advanced Interactions
document.addEventListener('DOMContentLoaded', () => {
    const neuralNetwork = document.getElementById('neuralNetwork');
    const hoverReflection = document.querySelector('.hover-reflection');
    const nodes = document.querySelectorAll('.node');
    const connections = document.querySelectorAll('.connection');
    
    let magnifiedNode = null;
    let sequenceInterval = null;
    let currentSequenceIndex = 0;
    let isSequenceActive = false;
    
    if (neuralNetwork && hoverReflection) {
        // Mouse move effect
        neuralNetwork.addEventListener('mousemove', (e) => {
            const rect = neuralNetwork.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            hoverReflection.style.left = x + 'px';
            hoverReflection.style.top = y + 'px';
            hoverReflection.style.opacity = '1';
        });
        
        neuralNetwork.addEventListener('mouseleave', () => {
            hoverReflection.style.opacity = '0';
            // Remove active states
            nodes.forEach(node => node.classList.remove('active'));
            connections.forEach(connection => connection.classList.remove('active'));
        });
        
        // Click to magnify functionality
        nodes.forEach(node => {
            node.addEventListener('click', (e) => {
                e.stopPropagation();
                
                // Remove previous magnified node
                if (magnifiedNode) {
                    magnifiedNode.classList.remove('magnified');
                    // Remove magnified connections
                    connections.forEach(conn => {
                        conn.classList.remove('magnified');
                    });
                }
                
                // Magnify clicked node
                node.classList.add('magnified');
                magnifiedNode = node;
                
                // Magnify connected connections
                const nodeNumber = node.getAttribute('data-node');
                connections.forEach(connection => {
                    const connectionNumber = connection.getAttribute('data-connection');
                    if (shouldActivateConnection(nodeNumber, connectionNumber)) {
                        connection.classList.add('magnified');
                    }
                });
                
                // Auto-remove magnification after 3 seconds
                setTimeout(() => {
                    if (magnifiedNode === node) {
                        node.classList.remove('magnified');
                        connections.forEach(conn => {
                            conn.classList.remove('magnified');
                        });
                        magnifiedNode = null;
                    }
                }, 3000);
            });
            
            node.addEventListener('mouseenter', () => {
                if (!magnifiedNode) {
                    node.classList.add('active');
                    // Activate connected connections
                    const nodeNumber = node.getAttribute('data-node');
                    connections.forEach(connection => {
                        const connectionNumber = connection.getAttribute('data-connection');
                        if (shouldActivateConnection(nodeNumber, connectionNumber)) {
                            connection.classList.add('active');
                        }
                    });
                }
            });
            
            node.addEventListener('mouseleave', () => {
                if (!magnifiedNode) {
                    node.classList.remove('active');
                    // Deactivate connections after a delay
                    setTimeout(() => {
                        connections.forEach(connection => {
                            connection.classList.remove('active');
                        });
                    }, 200);
                }
            });
        });
        
        // Connection hover effects
        connections.forEach(connection => {
            connection.addEventListener('mouseenter', () => {
                if (!magnifiedNode) {
                    connection.classList.add('active');
                }
            });
            
            connection.addEventListener('mouseleave', () => {
                if (!magnifiedNode) {
                    connection.classList.remove('active');
                }
            });
        });
        
        // Sequential animation on neural network hover
        neuralNetwork.addEventListener('mouseenter', () => {
            if (!isSequenceActive && !magnifiedNode) {
                startSequenceAnimation();
            }
        });
        
        neuralNetwork.addEventListener('mouseleave', () => {
            stopSequenceAnimation();
        });
        
        // Click outside to reset magnification
        document.addEventListener('click', (e) => {
            if (!neuralNetwork.contains(e.target) && magnifiedNode) {
                magnifiedNode.classList.remove('magnified');
                connections.forEach(conn => {
                    conn.classList.remove('magnified');
                });
                magnifiedNode = null;
            }
        });
    }
    
    function startSequenceAnimation() {
        isSequenceActive = true;
        currentSequenceIndex = 0;
        
        sequenceInterval = setInterval(() => {
            // Remove previous sequence states
            nodes.forEach(node => {
                node.classList.remove('sequence-active', 'sequence-prev');
            });
            connections.forEach(conn => {
                conn.classList.remove('sequence-active');
            });
            
            // Activate current node
            const currentNode = nodes[currentSequenceIndex];
            if (currentNode) {
                currentNode.classList.add('sequence-active');
                
                // Activate connected connections
                const nodeNumber = currentNode.getAttribute('data-node');
                connections.forEach(connection => {
                    const connectionNumber = connection.getAttribute('data-connection');
                    if (shouldActivateConnection(nodeNumber, connectionNumber)) {
                        connection.classList.add('sequence-active');
                    }
                });
                
                // Mark previous node as prev
                const prevIndex = currentSequenceIndex === 0 ? nodes.length - 1 : currentSequenceIndex - 1;
                nodes[prevIndex].classList.add('sequence-prev');
            }
            
            currentSequenceIndex = (currentSequenceIndex + 1) % nodes.length;
        }, 800);
    }
    
    function stopSequenceAnimation() {
        isSequenceActive = false;
        if (sequenceInterval) {
            clearInterval(sequenceInterval);
            sequenceInterval = null;
        }
        
        // Remove all sequence states
        nodes.forEach(node => {
            node.classList.remove('sequence-active', 'sequence-prev');
        });
        connections.forEach(conn => {
            conn.classList.remove('sequence-active');
        });
    }
});

// Helper function to determine which connections should be activated
function shouldActivateConnection(nodeNumber, connectionNumber) {
    const nodeConnections = {
        '1': ['1', '2'],
        '2': ['1', '2'],
        '3': ['3', '4'],
        '4': ['3', '4'],
        '5': ['5', '6'],
        '6': ['5', '6'],
        '7': ['1', '3', '5'],
        '8': ['2', '4', '6']
    };
    
    return nodeConnections[nodeNumber] && nodeConnections[nodeNumber].includes(connectionNumber);
}

// Add CSS for ripple animation
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
