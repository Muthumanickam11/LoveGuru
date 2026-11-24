import { useState, useRef, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import toast from 'react-hot-toast'
import ReactMarkdown from 'react-markdown'
import AppNavbar from '../components/common/AppNavbar'
import { chatApi } from '../api/apiCalls'
import { useChatStore } from '../store/chatStore'
import { useAuthStore } from '../store/authStore'

const STAGE_COLORS = {
  single: '#F59E0B',
  finding: '#10B981',
  relationship: '#3B82F6',
  heartbreak: '#F43F5E',
}

function TypingIndicator() {
  return (
    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-end', marginBottom: 12 }}>
      <div style={{
        width: 32, height: 32, borderRadius: '50%', flexShrink: 0,
        background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontSize: '0.9rem',
      }}>❤️</div>
      <div style={{
        padding: '12px 16px',
        background: 'rgba(255,255,255,0.04)',
        border: '1px solid rgba(255,255,255,0.08)',
        borderRadius: '16px 16px 16px 4px',
        display: 'flex', gap: 5, alignItems: 'center',
      }}>
        {[0, 1, 2].map((i) => (
          <div
            key={i}
            style={{
              width: 7, height: 7,
              background: '#94A3B8', borderRadius: '50%',
              animation: `typingBounce 1.4s ease infinite`,
              animationDelay: `${i * 0.2}s`,
            }}
          />
        ))}
      </div>
    </div>
  )
}

function Message({ msg }) {
  const isUser = msg.role === 'user'

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      style={{
        display: 'flex',
        justifyContent: isUser ? 'flex-end' : 'flex-start',
        alignItems: 'flex-end',
        gap: 8,
        marginBottom: 4,
      }}
    >
      {!isUser && (
        <div style={{
          width: 32, height: 32, borderRadius: '50%', flexShrink: 0,
          background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontSize: '0.9rem', alignSelf: 'flex-end',
        }}>❤️</div>
      )}
      <div style={{
        maxWidth: isUser ? '72%' : '78%',
        padding: isUser ? '10px 16px' : '14px 18px',
        background: isUser
          ? 'linear-gradient(135deg,#EC4899,#8B5CF6)'
          : 'rgba(255,255,255,0.04)',
        border: isUser ? 'none' : '1px solid rgba(255,255,255,0.08)',
        borderRadius: isUser
          ? '16px 16px 4px 16px'
          : '16px 16px 16px 4px',
        color: '#F0F4FF',
        fontSize: '0.95rem',
        lineHeight: 1.65,
        fontFamily: "'Plus Jakarta Sans', sans-serif",
        wordBreak: 'break-word',
      }}>
        {isUser ? (
          <div style={{ whiteSpace: 'pre-wrap' }}>{msg.content}</div>
        ) : (
          <div className="chat-markdown" style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <ReactMarkdown>{msg.content}</ReactMarkdown>
          </div>
        )}
      </div>
    </motion.div>
  )
}

export default function Chat() {
  const { conversationId } = useParams()
  const navigate = useNavigate()
  const { user } = useAuthStore()
  const {
    messages, isLoading, quickReplies, lastCrisisLevel,
    addUserMessage, appendAIMessage, setLoading, setCurrentSession,
  } = useChatStore()

  const [input, setInput] = useState('')
  const [currentConversationId, setCurrentConversationId] = useState(conversationId || null)
  const messagesEndRef = useRef(null)
  const textareaRef = useRef(null)
  const stage = user?.stage || 'single'
  const stageColor = STAGE_COLORS[stage] || '#EC4899'

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      textareaRef.current.style.height = Math.min(textareaRef.current.scrollHeight, 140) + 'px'
    }
  }, [input])

  const sendMessage = async (text) => {
    if (!text?.trim() || isLoading) return
    const messageText = text.trim()
    setInput('')
    addUserMessage(messageText)
    setLoading(true)

    try {
      const res = await chatApi.sendText({
        message: messageText,
        conversation_id: currentConversationId,
        mode: 'general',
      })
      const { response, conversation_id, quick_replies, crisis_level, emotion_detected } = res.data
      setCurrentConversationId(conversation_id)
      setCurrentSession(conversation_id)
      appendAIMessage(response, {
        quickReplies: quick_replies,
        crisisLevel: crisis_level,
        emotion: emotion_detected,
      })

      // Navigate to conversation URL
      if (!conversationId) {
        window.history.replaceState({}, '', `/chat/${conversation_id}`)
      }

      // Crisis alert
      if (crisis_level === 'critical' || crisis_level === 'high') {
        toast.error('💙 Crisis helplines are available 24/7 — iCall: 9152987821', {
          duration: 8000,
          id: 'crisis-toast',
        })
      }
    } catch (err) {
      toast.error('Connection issue. Please try again.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage(input)
    }
  }

  // Greeting for empty state
  const greeting = () => {
    const name = user?.display_name || 'friend'
    const hour = new Date().getHours()
    const timeGreet = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening'
    return `${timeGreet}, ${name}! I'm your LoveGuru. What's on your heart today? 💙`
  }

  return (
    <div className="page" style={{ height: '100vh', overflow: 'hidden' }}>
      <AppNavbar />

      <div style={{ flex: 1, display: 'flex', minHeight: 0 }}>

      {/* ── SIDEBAR ─────────────────────────────────────── */}
      <div style={{
        width: 260, flexShrink: 0,
        background: 'rgba(13,17,23,0.95)',
        borderRight: '1px solid rgba(255,255,255,0.06)',
        display: 'flex', flexDirection: 'column',
        padding: '20px 0',
      }}>
        {/* Sidebar header */}
        <div style={{
          padding: '0 20px 20px',
          borderBottom: '1px solid rgba(255,255,255,0.06)',
        }}>
          <div style={{
            fontFamily: "'Outfit', sans-serif", fontWeight: 700, fontSize: '0.95rem',
            color: '#F0F4FF',
          }}>Your Conversations</div>
          <div style={{ fontSize: '0.75rem', color: '#64748B', marginTop: 2 }}>
            Private &amp; confidential
          </div>
        </div>

        {/* New chat */}
        <div style={{ padding: '16px 12px' }}>
          <button
            id="new-chat-btn"
            onClick={() => {
              useChatStore.getState().clearMessages()
              setCurrentConversationId(null)
              navigate('/chat')
            }}
            style={{
              width: '100%', padding: '10px 16px',
              background: 'rgba(236,72,153,0.1)',
              border: '1px dashed rgba(236,72,153,0.3)',
              borderRadius: 12, color: '#EC4899',
              fontSize: '0.85rem', fontWeight: 600, cursor: 'pointer',
              fontFamily: "'Plus Jakarta Sans', sans-serif",
              display: 'flex', alignItems: 'center', gap: 8,
            }}
          >
            ✏️ New Conversation
          </button>
        </div>

        {/* Stage indicator */}
        <div style={{ padding: '0 12px', marginTop: 8 }}>
          <div style={{
            padding: '12px 16px',
            background: `${stageColor}15`,
            border: `1px solid ${stageColor}30`,
            borderRadius: 12,
          }}>
            <div style={{ color: stageColor, fontSize: '0.75rem', fontWeight: 600, marginBottom: 4 }}>
              CURRENT STAGE
            </div>
            <div style={{ color: '#F0F4FF', fontSize: '0.85rem', fontWeight: 600 }}>
              {stage === 'single' && '🟡 Single & Searching'}
              {stage === 'finding' && '🟢 Finding Love'}
              {stage === 'relationship' && '🔵 In Relationship'}
              {stage === 'heartbreak' && '🔴 After Breakup'}
            </div>
          </div>
        </div>

        {/* Spacer */}
        <div style={{ flex: 1 }} />

        {/* SOS button in sidebar */}
        <div style={{ padding: '12px' }}>
          <button
            id="sidebar-sos-btn"
            onClick={() => navigate('/emergency')}
            style={{
              width: '100%', padding: '10px',
              background: 'rgba(244,63,94,0.1)',
              border: '1px solid rgba(244,63,94,0.3)',
              borderRadius: 12, color: '#F43F5E',
              fontSize: '0.8rem', fontWeight: 600, cursor: 'pointer',
              fontFamily: "'Plus Jakarta Sans', sans-serif",
              display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8,
            }}
          >
            🆘 Crisis Support
          </button>
        </div>
      </div>

      {/* ── MAIN CHAT AREA ────────────────────────────── */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {/* Header */}
        <div style={{
          padding: '16px 24px',
          borderBottom: '1px solid rgba(255,255,255,0.06)',
          display: 'flex', alignItems: 'center', gap: 12,
          background: 'rgba(8,11,17,0.9)',
        }}>
          <div style={{
            width: 40, height: 40, borderRadius: '50%',
            background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontSize: '1.1rem', flexShrink: 0,
          }}>❤️</div>
          <div>
            <div style={{ color: '#F0F4FF', fontWeight: 700, fontSize: '0.95rem' }}>
              LoveGuru AI
            </div>
            <div style={{ color: '#10B981', fontSize: '0.75rem', fontWeight: 500, display: 'flex', alignItems: 'center', gap: 4 }}>
              <span style={{ width: 6, height: 6, background: '#10B981', borderRadius: '50%', display: 'inline-block' }} />
              Online · Always here for you
            </div>
          </div>
        </div>

        {/* Messages */}
        <div style={{
          flex: 1, overflowY: 'auto', padding: '24px',
          display: 'flex', flexDirection: 'column',
        }}>
          {messages.length === 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              style={{ textAlign: 'center', marginTop: 'auto', paddingBottom: 40 }}
            >
              <div style={{ fontSize: '3rem', marginBottom: 16, animation: 'float 3s ease-in-out infinite' }}>❤️</div>
              <div style={{
                maxWidth: 420, margin: '0 auto',
                padding: '20px 24px',
                background: 'rgba(255,255,255,0.03)',
                border: '1px solid rgba(255,255,255,0.07)',
                borderRadius: 20,
              }}>
                <p style={{ color: '#94A3B8', fontSize: '1rem', lineHeight: 1.65 }}>
                  {greeting()}
                </p>
              </div>
              {/* Quick starts */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, justifyContent: 'center', marginTop: 20 }}>
                {[
                  'I want to describe my dream partner',
                  'I just went through a breakup',
                  'My partner and I keep fighting',
                  'I need help with dating',
                ].map((prompt) => (
                  <button
                    key={prompt}
                    onClick={() => sendMessage(prompt)}
                    style={{
                      padding: '8px 16px',
                      background: 'rgba(255,255,255,0.04)',
                      border: '1px solid rgba(255,255,255,0.08)',
                      borderRadius: 999, color: '#94A3B8',
                      fontSize: '0.82rem', cursor: 'pointer',
                      fontFamily: "'Plus Jakarta Sans', sans-serif",
                      transition: 'all 0.2s',
                    }}
                    onMouseEnter={e => { e.target.style.background = 'rgba(236,72,153,0.1)'; e.target.style.borderColor = '#EC4899'; e.target.style.color = '#EC4899' }}
                    onMouseLeave={e => { e.target.style.background = 'rgba(255,255,255,0.04)'; e.target.style.borderColor = 'rgba(255,255,255,0.08)'; e.target.style.color = '#94A3B8' }}
                  >
                    {prompt}
                  </button>
                ))}
              </div>
            </motion.div>
          )}

          {messages.map((msg) => (
            <Message key={msg.id} msg={msg} />
          ))}

          {isLoading && <TypingIndicator />}

          {/* Quick replies */}
          {!isLoading && quickReplies.length > 0 && messages.length > 0 && (
            <div style={{
              display: 'flex', flexWrap: 'wrap', gap: 8,
              marginTop: 8, marginBottom: 8, paddingLeft: 40,
            }}>
              {quickReplies.map((reply) => (
                <button
                  key={reply}
                  onClick={() => sendMessage(reply)}
                  style={{
                    padding: '6px 14px',
                    background: 'rgba(255,255,255,0.04)',
                    border: '1px solid rgba(255,255,255,0.08)',
                    borderRadius: 999, color: '#94A3B8',
                    fontSize: '0.8rem', cursor: 'pointer',
                    fontFamily: "'Plus Jakarta Sans', sans-serif",
                    transition: 'all 0.2s',
                  }}
                  onMouseEnter={e => { e.target.style.background = 'rgba(236,72,153,0.1)'; e.target.style.color = '#EC4899'; e.target.style.borderColor = '#EC4899' }}
                  onMouseLeave={e => { e.target.style.background = 'rgba(255,255,255,0.04)'; e.target.style.color = '#94A3B8'; e.target.style.borderColor = 'rgba(255,255,255,0.08)' }}
                >
                  {reply}
                </button>
              ))}
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* ── INPUT BAR ──────────────────────────────────── */}
        <div style={{
          padding: '16px 24px',
          borderTop: '1px solid rgba(255,255,255,0.06)',
          background: 'rgba(8,11,17,0.95)',
        }}>
          <div style={{
            display: 'flex', gap: 10, alignItems: 'flex-end',
            background: 'rgba(22,29,42,0.9)',
            border: '1px solid rgba(255,255,255,0.08)',
            borderRadius: 16, padding: '8px 8px 8px 16px',
            transition: 'border-color 0.2s',
          }}
            onFocusCapture={e => e.currentTarget.style.borderColor = '#EC4899'}
            onBlurCapture={e => e.currentTarget.style.borderColor = 'rgba(255,255,255,0.08)'}
          >
            <textarea
              id="chat-input"
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Tell me what's on your heart... (Enter to send, Shift+Enter for new line)"
              disabled={isLoading}
              rows={1}
              style={{
                flex: 1, background: 'transparent', border: 'none',
                outline: 'none', color: '#F0F4FF', fontSize: '0.95rem',
                fontFamily: "'Plus Jakarta Sans', sans-serif",
                resize: 'none', lineHeight: 1.6,
                maxHeight: 140, overflowY: 'auto',
                padding: '6px 0',
              }}
            />
            {/* Image upload */}
            <button
              id="chat-image-btn"
              title="Upload image or screenshot"
              style={{
                width: 38, height: 38, borderRadius: 10, border: 'none',
                background: 'rgba(255,255,255,0.06)',
                color: '#475569', cursor: 'pointer', fontSize: '1rem',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                flexShrink: 0, transition: 'all 0.2s',
              }}
              onMouseEnter={e => { e.target.style.background = 'rgba(255,255,255,0.1)'; e.target.style.color = '#94A3B8' }}
              onMouseLeave={e => { e.target.style.background = 'rgba(255,255,255,0.06)'; e.target.style.color = '#475569' }}
            >📷</button>
            {/* Send */}
            <button
              id="chat-send-btn"
              onClick={() => sendMessage(input)}
              disabled={!input.trim() || isLoading}
              style={{
                width: 38, height: 38, borderRadius: 10, border: 'none',
                background: input.trim() && !isLoading
                  ? 'linear-gradient(135deg,#EC4899,#8B5CF6)'
                  : 'rgba(255,255,255,0.06)',
                color: input.trim() && !isLoading ? '#fff' : '#475569',
                cursor: input.trim() && !isLoading ? 'pointer' : 'not-allowed',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                flexShrink: 0, transition: 'all 0.2s', fontSize: '1rem',
              }}
            >
              {isLoading ? '⏳' : '→'}
            </button>
          </div>
          <div style={{ color: '#334155', fontSize: '0.72rem', marginTop: 8, textAlign: 'center' }}>
            LoveGuru AI is not a replacement for therapy. Crisis support: iCall 9152987821 (24/7)
          </div>
        </div>
      </div>
      </div>
    </div>
  )
}
