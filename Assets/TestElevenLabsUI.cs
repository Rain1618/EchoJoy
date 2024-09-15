using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;
using UnityEngine.Events;

public class TestElevenLabsUI : MonoBehaviour
{
    
    public Button sendButton;
    public InputField inputField;
    public ElevenLabsAPI tts;
    
    void Start()
    {
        if (tts == null)
            Debug.LogError("tts is not assigned!");
        if (sendButton == null)
            Debug.LogError("sendButton is not assigned!");
        if (inputField == null)
            Debug.LogError("inputField is not assigned!");

        // Add the PlayClip handler to the ElevenLabsAPI script
        tts.AudioReceived.AddListener(PlayClip);
        
        // Add the Button's onClick handler 
        sendButton.onClick.AddListener( () => {
            tts.GetAudio(inputField.text);
            inputField.text = "";
        });
    }

    public void PlayClip(AudioClip clip)
    {
        AudioSource.PlayClipAtPoint(clip, Camera.main.transform.position);
    }
}
