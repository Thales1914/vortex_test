document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://127.0.0.1:8000';

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = '';

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (password.length < 8 || !/\d/.test(password) || !/[a-zA-Z]/.test(password)) {
                errorMessage.textContent = 'A senha não atende aos requisitos.';
                return;
            }

            const urlParams = new URLSearchParams(window.location.search);
            const referrerId = urlParams.get('ref');
            
            let registerUrl = `${API_URL}/register/`;
            if (referrerId) {
                registerUrl += `?referrer_id=${referrerId}`;
            }

            try {
                const response = await fetch(registerUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ name, email, password }),
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Falha ao cadastrar');
                }

                const userData = await response.json();
                
                localStorage.setItem('userId', userData.id);
                window.location.href = 'profile.html';

            } catch (error) {
                errorMessage.textContent = error.message;
            }
        });
    }

    if (window.location.pathname.endsWith('profile.html')) {
        const userId = localStorage.getItem('userId');
        if (!userId) {
            window.location.href = 'index.html';
            return;
        }

        fetch(`${API_URL}/users/${userId}`)
            .then(response => {
                if (!response.ok) throw new Error('Usuário não encontrado');
                return response.json();
            })
            .then(data => {
                document.getElementById('userName').textContent = data.name;
                document.getElementById('userScore').textContent = data.score;
                document.getElementById('referralLink').value = data.referral_link;
            })
            .catch(error => {
                console.error('Erro ao buscar dados do perfil:', error);
                localStorage.removeItem('userId');
                window.location.href = 'index.html';
            });
        
        const copyButton = document.getElementById('copyButton');
        copyButton.addEventListener('click', () => {
            const referralLink = document.getElementById('referralLink');
            referralLink.select();
            document.execCommand('copy');
            
            const copySuccessMessage = document.getElementById('copy-success');
            copySuccessMessage.textContent = 'Link copiado!';
            setTimeout(() => {
                copySuccessMessage.textContent = '';
            }, 2000);
        });
    }
});